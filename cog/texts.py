from utils.imports import *


FAQ_CONTENT = """
# FAQ

## 1. General

### Will there be an iOS version?
> No.

### Will Usagi ever be on the Google Play Store?
> No.

### Can Usagi read Light Novels?
> No.

### Can Usagi stream Anime?
> No.

### Can Usagi sync between devices?
> Yes.

### Can I apply backups from Tachiyomi to Usagi?
> Possibly, but not officially.


## 2. Sources

### What are some recommended sources? What source is the best? What is the replacement for source X? Where to read manga Y?
> No.

### I'm having an issue with X source
> No. That's not our fault.


## 3. Other

### Q: Why does Usagi no longer integrate sources like Kotatsu did before?
I decided to remove the library that has built-in Online sources for the following reasons:

> 1. DMCA violation: This is a strong VIOLATION of copyrighted content, causing many applications to be forced to close like Tachiyomi, Kotatsu* before.
> 2. Disadvantage: Users always feel uncomfortable when frequently encountering reading source problems. They are forced to wait until the next app update is released so the problem can be fixed.
> 3. Development: Programmers / Contributors have always found it difficult to run Tests on previous applications, they did not have many options. Most of them follow previous testing methods such as running directly on the integrated library (cannot test all cases) OR they are forced to build test applications (like Kotatsu Dev) to be able to test content after implement.
> 4. Forced removal of reported content: According to #39 on the old integrated library, some content was forced to be taken down at the owner's request, making it impossible for users to continue accessing that content.
> 5. Privacy: In some cases, some content has been hidden / encrypted by the owner, and you are allowed to exploit it by the owner. But the old built-in library is an open source library based on the GPL-3.0 license, which requires the library's source code to be completely public. From there, passwords, hidden tokens, decryption methods, etc. will be forced to be made public on the source code, allowing others to exploit them.
-# *Kotatsu is said to be a branch of Tachiyomi based on document number 8 of Kakao Ent. (P. Cok)


### Q: Can Usagi work without a Plugin?
> Yes. Usagi works as an offline manga reader, able to read .CBZ files, manga image folders and even PDF* files

-# *in the future, soon.


### Q: Does Usagi have anything to do with other apps?
> Usagi is a standalone / another fork of Kotatsu, not relying on any other application. I got ideas from many applications, but it's not related to any application.


### Q: Who created Usagi? Which team / project does it belong to?
> <@954613690638929970>. Usagi is a product of the Yumemi™ project.


### Q: Does Usagi have anything to do with any other organization?
> No, it doesn't. Usagi itself can operate independently without involving any libraries / organizations outside of Usagi (except some android open source libraries for Usagi development)

-# ©️ 2026 Usagi
"""


class FAQView(discord.ui.DesignerView):
    def __init__(self):
        super().__init__(timeout=None)

        self.link_rules = discord.ui.Button(
            style=discord.ButtonStyle.link,
            url="https://discord.com/channels/1484655684879519885/1484655685542350990",
            label="Rules",
            emoji="📚",
        )

        self.link_faq = discord.ui.Button(
            style=discord.ButtonStyle.link,
            url="https://discord.com/channels/1484655684879519885/1507099046265880787",
            label="Information",
            emoji="ℹ️",
        )

        section = discord.ui.Section(
            discord.ui.TextDisplay(
                content=FAQ_CONTENT
            ),
            accessory=discord.ui.Thumbnail(
                "https://cdn.discordapp.com/attachments/1487153908550729748/1507140038935449641/faq-svgrepo-com.png?ex=6a10d10a&is=6a0f7f8a&hm=b0fb5ef927d53ea1a7c66b38238eef70b98c14f9344bbb445f9f38117974667d&"
            )
        )

        container = discord.ui.Container(
            section,
            color=discord.Color.ash_theme(),
        )

        row = discord.ui.ActionRow(
            self.link_rules,
            self.link_faq
        )

        self.add_item(container)
        self.add_item(row)


class FAQ(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._view_registered = False

    @commands.Cog.listener()
    async def on_ready(self):

        if not self._view_registered:
            self.bot.add_view(InformationView())

            self._view_registered = True

    @slash_command()
    @commands.is_owner()
    async def faq(self, ctx: discord.ApplicationContext) -> None:

        await ctx.respond(
            "...",
            ephemeral=True,
        )

        await ctx.channel.send(
            view=FAQView(),
            allowed_mentions=discord.AllowedMentions.none(),
        )


    @slash_command()
    @commands.is_owner()
    async def rules(self, ctx: discord.ApplicationContext) -> None:

        await ctx.respond(
            "...",
            ephemeral=True,
        )

        await ctx.channel.send(
            view=RulesView()
        )

    @slash_command()
    @commands.is_owner()
    async def information(self, ctx: discord.ApplicationContext) -> None:

        await ctx.respond(
            "...",
            ephemeral=True,
        )

        await ctx.channel.send(
            view=InformationView()
        )


def setup(bot):
    bot.add_cog(FAQ(bot))

class RulesView(discord.ui.DesignerView):
    def __init__(self):
        super().__init__(timeout=None)

        self.link_information = discord.ui.Button(
            style=discord.ButtonStyle.link,
            url="https://discord.com/channels/1484655684879519885/1507099046265880787",
            label="Information",
            emoji="ℹ️",
        )

        self.link_faq = discord.ui.Button(
            style=discord.ButtonStyle.link,
            url="https://discord.com/channels/1484655684879519885/1487524792738512906",
            label="FAQ",
            emoji="❓",
        )

        container = discord.ui.Container(

            discord.ui.Section(
                discord.ui.TextDisplay(
                    """
# Rules
1. Do not attempt to bypass filters or safety systems.
2. No advertising.
3. No AI.
4. Do not request or suggest external sources, plugins, or integrations.
5. Follow Discord Terms of Service at all times: **[ToS Link](https://discord.com/terms)**
                    """
                ),

                accessory=discord.ui.Thumbnail(
                    "https://cdn.discordapp.com/attachments/1487153908550729748/1507133957853024266/book-bookmark-svgrepo-com1.png"
                ),
            ),

            discord.ui.Separator(
                divider=True,
                spacing=discord.SeparatorSpacingSize.small,
            ),

            discord.ui.TextDisplay(
                """
# Notes
- These rules may not apply to all i18n channels.
- Always check the specific channel rules if available.
-# Do not offend communism... writen from a communist
                """
            ),

            color=discord.Color.green(),
        )

        row = discord.ui.ActionRow(
            self.link_information,
            self.link_faq
        )

        self.add_item(container)
        self.add_item(row)


class InformationView(discord.ui.DesignerView):
    def __init__(self):
        super().__init__(timeout=None)

        self.role_id = 1507330930686165063

        thumbnail = discord.ui.Thumbnail(
            "https://cdn.discordapp.com/attachments/1487153908550729748/1507340740361982002/info-square-svgrepo-com1.png"
        )

        self.link_rules = discord.ui.Button(
            style=discord.ButtonStyle.link,
            url="https://discord.com/channels/1484655684879519885/1484655685542350990",
            label="Rules",
            emoji="📚",
        )

        self.link_faq = discord.ui.Button(
            style=discord.ButtonStyle.link,
            url="https://discord.com/channels/1484655684879519885/1487524792738512906",
            label="FAQ",
            emoji="❓",
        )


        self.link_button = discord.ui.Button(
            style=discord.ButtonStyle.blurple,
            emoji="👥",
            custom_id="link_button",
        )

        self.role_button = discord.ui.Button(
            style=discord.ButtonStyle.green,
            emoji="⭐",
            custom_id="role_button",
        )

        self.plugin_role_button = discord.ui.Button(
            style=discord.ButtonStyle.grey,
            emoji="📑",
            custom_id="plugin_role_button",
        )

        self.link_button.callback = self.link_callback
        self.role_button.callback = self.role_callback
        self.plugin_role_button.callback = self.plugin_role_callback

        container = discord.ui.Container(
            discord.ui.Section(
                discord.ui.TextDisplay(
                    """
# Information

*Click on the buttons for further Infos*
-# If you press on `📑` you will get a Role...
                    """
                ),
                accessory=thumbnail,
            ),

            discord.ui.Section(
                discord.ui.TextDisplay("Permanent Server Invite Link"),
                accessory=self.link_button,
            ),

            discord.ui.Separator(
                divider=True,
                spacing=discord.SeparatorSpacingSize.small,
            ),

            discord.ui.Section(
                discord.ui.TextDisplay("Role Info & Rewards"),
                accessory=self.role_button,
            ),

            discord.ui.Separator(
                divider=True,
                spacing=discord.SeparatorSpacingSize.small,
            ),

            discord.ui.Section(
                discord.ui.TextDisplay("Plugin Creator Role"),
                accessory=self.plugin_role_button,
            ),

            color=discord.Color.blurple(),
        )

        row = discord.ui.ActionRow(
            self.link_rules,
            self.link_faq
        )

        self.add_item(container)
        self.add_item(row)

    async def link_callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            "Link to join Usagi Discord server (fixed): https://discord.gg/4AHskjwtj4",
            ephemeral=True
        )

    async def role_callback(self, interaction: discord.Interaction):
        text = """
# Leveling Infos
Lvl. 1 - <@&1506622205155348680>
[+] Attach files
                
Lvl. 3. - <@&1506622232946933800>
[+] Create public threads
                
Lvl. 5 - <@&1506622265578623006>
[+] be build diff.
                
Lvl.10 - <@&1506622288836034680>
[+] High class
                
Lvl.15 - <@&1506622319341342832>
[+] Noble
                
Lvl.20 - <@&1506622340828631050>
[+] Unemployment boss

-# All those extra perms are stacked.
-# Any idea for perms ping the communist.

# Booster Information

Our god whoever boosts.

# General Role Information

Project Owner - <@&1486482350320779416>
- Owner.

Deisgners - <@&1505996941719371890>
- Nice designs. 👍

Mods - <@&1485941316511727737>
- The slaves.

Supporters - <@&1484673277988306974>
- idk?


Contributor - <@&1507858099384615055>
- App contributions / project contributions

Translator - <@&1507858349285179513>
- Translation work within the project

*Important notes for Contributors & Translators:*
-# Minor changes do not automatically qualify, final decision is up to the dev team
-# Always provide a link to the related GitHub PR or comment
-# After that, post a message here: https://discord.com/channels/1484655684879519885/1488486579872989294 and ping <@809739434537910283> (all in one message pls.)
        """
        return await interaction.response.send_message(text, ephemeral=True)

    async def plugin_role_callback(self, interaction: discord.Interaction):
        role = interaction.guild.get_role(self.role_id)

        if not role:
            return await interaction.response.send_message("Role not found.", ephemeral=True)

        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)
            return await interaction.response.send_message("You clicked it again? Alright you greedy b*tch, I removed the role. <3", ephemeral=True)

        await interaction.user.add_roles(role)
        return await interaction.response.send_message("Yayyy you are a creator now. What this role can do? No idea.", ephemeral=True)
