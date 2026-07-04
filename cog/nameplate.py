from typing import TYPE_CHECKING

import aiohttp
import discord
from pydantic import BaseModel, Field, ValidationError, field_validator, model_validator

import logging
base_logger = logging.getLogger(__name__)
logger = base_logger.getChild("nameplate")
if TYPE_CHECKING:
    from logging import custom

default: dict[str, bool] = {"enabled": True}
logger = base_logger.getChild("namestyle")

VALID_FONT_IDS: set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
VALID_EFFECT_IDS: set[int] = {1, 2, 3, 4, 5, 6}


class DisplayNameStylePayload(BaseModel):
    font_id: int | None = None
    effect_id: int | None = None
    colors: list[int] = Field(default_factory=list, max_length=2)

    @field_validator("font_id")
    @classmethod
    def validate_font_id(cls, value: int | None) -> int | None:
        if value is None:
            return None
        if value not in VALID_FONT_IDS:
            raise ValueError(f"font_id must be one of {sorted(VALID_FONT_IDS)}")
        return value

    @field_validator("effect_id")
    @classmethod
    def validate_effect_id(cls, value: int | None) -> int | None:
        if value is None:
            return None
        if value not in VALID_EFFECT_IDS:
            raise ValueError(f"effect_id must be one of {sorted(VALID_EFFECT_IDS)}")
        return value

    @field_validator("colors")
    @classmethod
    def validate_colors(cls, colors: list[int]) -> list[int]:
        for color in colors:
            if color < 0 or color > 0xFFFFFF:
                raise ValueError("Each color must be between 0x000000 and 0xFFFFFF.")
        return colors

    @model_validator(mode="after")
    def validate_effect_color_combo(self) -> "DisplayNameStylePayload":
        if self.effect_id == 2 and len(self.colors) != 2:
            raise ValueError("effect_id=2 (GRADIENT) requires exactly 2 colors.")
        if self.effect_id in {1, 3, 4, 5, 6} and len(self.colors) < 1:
            raise ValueError("effect_id requires at least 1 color.")
        return self

    def to_patch_payload(self) -> dict[str, object]:
        payload: dict[str, object] = {}
        if self.font_id is not None:
            payload["display_name_font_id"] = self.font_id
        if self.effect_id is not None:
            payload["display_name_effect_id"] = self.effect_id
        if self.colors:
            payload["display_name_colors"] = self.colors
        return payload

    def to_style_payload(self) -> dict[str, object]:
        payload: dict[str, object] = {}
        if self.font_id is not None:
            payload["font_id"] = self.font_id
        if self.effect_id is not None:
            payload["effect_id"] = self.effect_id
        if self.colors:
            payload["colors"] = self.colors
        return payload


class NameStyleCog(discord.Cog):
    def __init__(self, bot: discord.Bot) -> None:
        self.bot = bot

    @staticmethod
    def parse_color(color: str) -> int:
        cleaned = color.strip().lstrip("#")
        if len(cleaned) != 6:
            raise ValueError("Color must be in RRGGBB format.")
        return int(cleaned, 16)

    @staticmethod
    def get_clear_payload() -> dict[str, object]:
        return {
            "display_name_font_id": None,
            "display_name_effect_id": None,
            "display_name_colors": None,
        }

    async def parse_colors(
        self,
        ctx: discord.ApplicationContext,
        primary_color: str | None,
        secondary_color: str | None,
    ) -> list[int] | None:
        colors: list[int] = []
        try:
            if primary_color:
                colors.append(self.parse_color(primary_color))
            if secondary_color:
                colors.append(self.parse_color(secondary_color))
        except ValueError:
            logger.debug(
                "namestyle color validation failed for user=%s guild=%s primary=%s secondary=%s",
                ctx.author.id,
                ctx.guild.id,
                primary_color,
                secondary_color,
            )
            await ctx.respond("Invalid color. Use RRGGBB or #RRGGBB.", ephemeral=True)
            return None

        return colors

    async def build_style_payloads(
        self,
        ctx: discord.ApplicationContext,
        *,
        font_id: int | None,
        effect_id: int | None,
        primary_color: str | None,
        secondary_color: str | None,
        clear: bool,
    ) -> tuple[dict[str, object], dict[str, object]] | None:
        if clear:
            return self.get_clear_payload(), {}

        colors = await self.parse_colors(ctx, primary_color, secondary_color)
        if colors is None:
            return None

        try:
            style_model = DisplayNameStylePayload(font_id=font_id, effect_id=effect_id, colors=colors)
        except ValidationError as exc:
            errors = "; ".join(error["msg"] for error in exc.errors())
            logger.debug(
                "namestyle pydantic validation failed user=%s guild=%s errors=%s",
                ctx.author.id,
                ctx.guild.id,
                errors,
            )
            await ctx.respond(f"Invalid style options: {errors}", ephemeral=True)
            return None

        return style_model.to_patch_payload(), style_model.to_style_payload()

    async def patch_member_style(
        self,
        *,
        ctx: discord.ApplicationContext,
        payload: dict[str, object],
    ) -> tuple[int, dict[str, object] | None]:
        token = getattr(self.bot.http, "token", None)
        if not token:
            logger.error("namestyle missing bot token user=%s guild=%s", ctx.author.id, ctx.guild.id)
            await ctx.respond("Missing Bot token", ephemeral=True)
            return 0, None

        url = f"https://discord.com/api/guilds/{ctx.guild.id}/members/@me"
        headers = {"Authorization": f"Bot {token}", "Content-Type": "application/json"}

        async with aiohttp.ClientSession(headers=headers) as session, session.patch(url, json=payload) as resp:
            response_text = await resp.text()
            if resp.status >= 400:
                logger.error(
                    "namestyle API call failed user=%s guild=%s status=%s payload=%s response=%s",
                    ctx.author.id,
                    ctx.guild.id,
                    resp.status,
                    payload,
                    response_text,
                )
                return resp.status, None

            try:
                response_data = await resp.json()
            except aiohttp.ContentTypeError:
                response_data = {}

            logger.debug(
                "namestyle API call succeeded user=%s guild=%s status=%s response_display_name_styles=%s",
                ctx.author.id,
                ctx.guild.id,
                resp.status,
                (response_data or {}).get("display_name_styles"),
            )
            return resp.status, response_data

    async def apply_style_with_fallback(
        self,
        *,
        ctx: discord.ApplicationContext,
        clear: bool,
        payload: dict[str, object],
        style_payload: dict[str, object],
    ) -> tuple[int, dict[str, object] | None]:
        status, response = await self.patch_member_style(ctx=ctx, payload=payload)
        if status >= 400 or clear or not style_payload:
            return status, response

        if not isinstance(response, dict) or response.get("display_name_styles") is not None:
            return status, response

        fallback_payload: dict[str, object] = {"display_name_styles": style_payload}
        logger.debug(
            "namestyle response has no display_name_styles, trying fallback user=%s guild=%s payload=%s",
            ctx.author.id,
            ctx.guild.id,
            fallback_payload,
        )
        return await self.patch_member_style(ctx=ctx, payload=fallback_payload)

    @discord.slash_command(  # pyright: ignore[reportUntypedFunctionDecorator]
        name="namestyle",
        contexts={discord.InteractionContextType.guild},
    )
    async def namestyle(
        self,
        ctx: discord.ApplicationContext,
        font_id: int | None = None,
        effect_id: int | None = None,
        primary_color: str | None = None,
        secondary_color: str | None = None,
        clear: bool = False,
    ) -> None:
        logger.debug(
            "namestyle called by user=%s guild=%s clear=%s font_id=%s effect_id=%s primary_color=%s secondary_color=%s",
            getattr(ctx.author, "id", "unknown"),
            getattr(ctx.guild, "id", "unknown"),
            clear,
            font_id,
            effect_id,
            primary_color,
            secondary_color,
        )
        if ctx.guild is None:
            await ctx.respond("Guild only.", ephemeral=True)
            return

        payloads = await self.build_style_payloads(
            ctx,
            font_id=font_id,
            effect_id=effect_id,
            primary_color=primary_color,
            secondary_color=secondary_color,
            clear=clear,
        )
        if payloads is None:
            return

        payload, style_payload = payloads
        if not payload:
            logger.debug("namestyle empty payload for user=%s guild=%s", ctx.author.id, ctx.guild.id)
            await ctx.respond("nothing to update.", ephemeral=True)
            return

        logger.debug(
            "namestyle payload built user=%s guild=%s payload=%s style_payload=%s",
            ctx.author.id,
            ctx.guild.id,
            payload,
            style_payload,
        )
        await ctx.defer(ephemeral=True)
        status, _ = await self.apply_style_with_fallback(
            ctx=ctx,
            clear=clear,
            payload=payload,
            style_payload=style_payload,
        )
        if status >= 400:
            await ctx.respond(f"failed status {status}", ephemeral=True)
            return

        await ctx.respond("updated.", ephemeral=True)


def setup(bot: discord.Bot) -> None:
    bot.add_cog(NameStyleCog(bot=bot))


__all__ = ["default", "setup"]
