from utils.imports import *


FAQ1 = """
# ❓ FAQ
## 🌐 General

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
"""

FAQ2 = """
## 🔍 Sources

### What are some recommended sources? What source is the best? What is the replacement for source X? Where to read manga Y?
> No.

### I'm having an issue with X source
> No. That's not our fault.
"""

FAQ3 = """
## 🗂️ Other

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

        self.link_announcements = discord.ui.Button(
            style=discord.ButtonStyle.link,
            url="https://discord.com/channels/1484655684879519885/1484655685542350991",
            label="Download Latest Update",
            emoji="🔄",
        )

        self.link_roles = discord.ui.Button(
            style=discord.ButtonStyle.link,
            url="https://discord.com/channels/1484655684879519885/1507099046265880787",
            label="Roles",
            emoji="🔥",
        )

        container1 = discord.ui.Container(
            discord.ui.Section(
                discord.ui.TextDisplay(
                    content=FAQ1
                ),
                accessory=discord.ui.Thumbnail(
                    "https://cdn.discordapp.com/attachments/1487153908550729748/1507140038935449641/faq-svgrepo-com.png?ex=6a10d10a&is=6a0f7f8a&hm=b0fb5ef927d53ea1a7c66b38238eef70b98c14f9344bbb445f9f38117974667d&"
                )
            )
        )

        container2 = discord.ui.Container(
            discord.ui.TextDisplay(
                content=FAQ2
            )
        )
        container3 = discord.ui.Container(
            discord.ui.TextDisplay(
                content=FAQ3
            )
        )

        row = discord.ui.ActionRow(
            self.link_rules,
            self.link_announcements,
            self.link_roles,
        )

        self.add_item(container1)
        self.add_item(container2)
        self.add_item(container3)
        self.add_item(row)


class RulesView(discord.ui.DesignerView):
    def __init__(self):
        super().__init__(timeout=None)

        self.link_roles = discord.ui.Button(
            style=discord.ButtonStyle.link,
            url="https://discord.com/channels/1484655684879519885/1507099046265880787",
            label="Roles",
            emoji="🔥",
        )

        self.link_announcements = discord.ui.Button(
            style=discord.ButtonStyle.link,
            url="https://discord.com/channels/1484655684879519885/1484655685542350991",
            label="Download Latest Update",
            emoji="🔄",
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

        )

        row = discord.ui.ActionRow(
            self.link_announcements,
            self.link_roles,
            self.link_faq
        )

        self.add_item(container)
        self.add_item(row)


class RolesView(discord.ui.DesignerView):
    def __init__(self):
        super().__init__(timeout=None)

        self.role_id = 1507330930686165063

        self.link_rules = discord.ui.Button(
            style=discord.ButtonStyle.link,
            url="https://discord.com/channels/1484655684879519885/1484655685542350990",
            label="Rules",
            emoji="📚",
        )

        self.link_announcements = discord.ui.Button(
            style=discord.ButtonStyle.link,
            url="https://discord.com/channels/1484655684879519885/1484655685542350991",
            label="Download Latest Update",
            emoji="🔄",
        )

        self.link_faq = discord.ui.Button(
            style=discord.ButtonStyle.link,
            url="https://discord.com/channels/1484655684879519885/1487524792738512906",
            label="FAQ",
            emoji="❓",
        )

        self.plugin_role_button = discord.ui.Button(
            style=discord.ButtonStyle.red,
            emoji="🐦‍🔥",
            custom_id="plugin_role_button",
        )

        self.plugin_role_button.callback = self.plugin_role_callback

        container1 = discord.ui.Container(
            discord.ui.TextDisplay(
                content="""
# 🔥 Roles
-  **Tip:** Check out <id:customize> to select roles.
-# - If you are eligible for a role, simply contact an admin or moderator once you have fulfilled the requirements.
                    """
            ),

            discord.ui.ActionRow(
                discord.ui.Button(
                    style=discord.ButtonStyle.link,
                    url="https://discord.com/channels/1484655684879519885/1488486579872989294",
                    label="Click here to requests",
                    emoji="📝",
                ),
            ),

            discord.ui.Separator(
                divider=True,
                spacing=discord.SeparatorSpacingSize.small,
            ),

            discord.ui.TextDisplay(
                content="""
## 🚬 Server Team

- <@&1486482350320779416> - Owner.
- <@&1505996941719371890> - Designs for our Server & Project. --> <@1031544793706274837>
- <@&1485941316511727737> - The slaves that ensures everyone compliance with the rules.
- <@&1484673277988306974> - Helpers of the Mods.

## 🛠️ Helpers
- <@&1507858099384615055> - App contributions / project contributions: [Github](https://github.com/UsagiApp)
- <@&1507858349285179513> - Translation for the project: [Weblate](https://hosted.weblate.org/projects/usagi/)

-# - Minor changes do not automatically qualify, final decision is up to the dev team.
-# - Always provide a link to the related GitHub PR or comment.  `(Check first sentence how to requests)`                 

## 🏆 Reward Roles
- <@&1504377838361383003> - Our gods whoever boosts.
- <@&1507330930686165063> - Unknown.
-# Press maybe the `🐦‍🔥` button.
                    """
            ),
        )

        container2 = discord.ui.Container(
            discord.ui.TextDisplay(
                content="""
## ⭐ Level
-# - Use </rank:1287124581131485330> in https://discord.com/channels/1484655684879519885/1508055170418999387 to see your rank.

<@&1506622205155348680> - Lvl. 1
[+] Change nickname

<@&1506622232946933800> - Lvl. 3
[+] Create public threads
[+] Attach files

<@&1506622265578623006> - Lvl. 5
[+] Create polls

<@&1506622288836034680> - Lvl. 10
[+] Soundboard permisions

<@&1506622319341342832> - Lvl. 15
[+] Add an emoji / sticker / soundboard `(contact a mod)`

<@&1506622340828631050> - Lvl. 20
[+] Unemployment boss
                """
            )
        )

        container3 = discord.ui.Container(
            discord.ui.TextDisplay(
                content="""
# 📝 Join us as Developer / Designer
Click the button below to message <@809739434537910283> for further communication.
                """
            ),
            discord.ui.ActionRow(
                discord.ui.Button(
                    style=discord.ButtonStyle.link,
                    url="https://discord.com/channels/@me/809739434537910283",
                    label="Join now",
                    emoji="📝",
                ),
            ),
            color=discord.Color.orange(),
        )

        row = discord.ui.ActionRow(
            self.link_rules,
            self.link_announcements,
            self.link_faq,
            self.plugin_role_button
        )



        self.add_item(container1)
        self.add_item(container2)
        self.add_item(container3)
        self.add_item(row)

    async def plugin_role_callback(self, interaction: discord.Interaction):
        role = interaction.guild.get_role(self.role_id)

        if not role:
            return await interaction.response.send_message("Role not found.", ephemeral=True)

        if role in interaction.user.roles:
            await interaction.user.remove_roles(role, reason="button")
            return await interaction.response.send_message(
                "You clicked it again? Alright you greedy b*tch, I removed the role. <3", ephemeral=True)

        await interaction.user.add_roles(role, reason="button")
        return await interaction.response.send_message("Yayyy you are a creator now. What this role can do? No idea.",
                                                       ephemeral=True)

ISSUES_LANGUAGES = {
    "en": {
        "container1": """
# 🌍 ENGLISH
-# - 🇷🇺 RUSSIAN & 🇻🇳 VIETNAM below use button

### Read NOTES before submitting.
""",
        "container2": """
## 🧾 ISSUE REPORT
- Name: Problem
- Description *(required)*
- App version *(required)*
- Steps to reproduce *(required)*
- Frequency *(required)*
- Device/ROM *(optional)*
- Screenshot / video *(if needed)*

-# ⚠️ Not for sync or update chapter issues.
""",

        "container3": """
## ❓ QUESTION
- Name: Question
- Description *(required)*
- App version *(required)*
- Screenshot / video *(if needed)*
-# --> Use for that please https://discord.com/channels/1484655684879519885/1488486579872989294!

-# ⚠️ Only feature questions, no requests/suggestions.
""",

        "container4": """
## 🔄 SYNC ISSUE
- Name: Sync Problem
- Description *(required)*
- App version *(required)*
- Device/ROM *(required)*
- Frequency *(required)*
- Screenshot / video *(if needed)*
""",

        "container5": """
## 📚 UPDATE CHAPTERS
- Name: Update Chapters Problem
- Description *(required)*
- App version *(required)*
- Frequency *(required)*
- Update log screenshot *(required)*
- Extra proof *(if needed)*

### ⚠️ NOTES
-# - Only latest version supported → https://discord.com/channels/1484655684879519885/1484655685542350991
-# - Use only **one tag**
-# - Template may change — always check updates
""",
    },

    "ru": {
        "container1": """
# 🌍 РУССКИЙ

### Прочитайте NOTES перед отправкой.
    """,

        "container2": """
## 🧾 ОТЧЁТ ОБ ОШИБКЕ
- Название: Проблема
- Описание *(обязательно)*
- Версия приложения *(обязательно)*
- Шаги для воспроизведения *(обязательно)*
- Частота возникновения *(обязательно)*
- Устройство / Прошивка *(необязательно)*
- Скриншот / Видео *(при необходимости)*

-# ⚠️ Не для проблем с синхронизацией или обновлением глав.
    """,

        "container3": """
## ❓ ВОПРОС
- Название: Вопрос
- Описание *(обязательно)*
- Версия приложения *(обязательно)*
- Скриншот / видео *(при необходимости)*
-# --> Для этого используйте пожалуйста https://discord.com/channels/1484655684879519885/1488486579872989294!

-# ⚠️ Только вопросы о функциях, без запросов/предложений.
    """,

        "container4": """
## 🔄 ПРОБЛЕМА С СИНХРОНИЗАЦИЕЙ
- Название: Проблема с синхронизацией
- Описание *(обязательно)*
- Версия приложения *(обязательно)*
- Устройство / ROM *(обязательно)*
- Частота возникновения *(обязательно)*
- Скриншот / видео *(при необходимости)*
    """,

        "container5": """
## 📚 ОБНОВЛЕНИЕ ГЛАВ
- Название: Проблема с обновлением глав
- Описание *(обязательно)*
- Версия приложения *(обязательно)*
- Частота возникновения *(обязательно)*
- Скриншот журнала обновлений *(обязательно)*
- Дополнительные доказательства *(при необходимости)*

### ⚠️ NOTES
-# - Поддерживается только последняя версия → https://discord.com/channels/1484655684879519885/1484655685542350991
-# - Используйте только **один тег**
-# - Шаблон может измениться — всегда проверяйте обновления
    """,
    },

    "vi": {
        "container1": """
# 🌍 VIỆT NAM

### Đọc NOTES trước khi gửi.
    """,

        "container2": """
## 🧾 BÁO CÁO LỖI
- Tên: Vấn đề
- Mô tả *(bắt buộc)*
- Phiên bản ứng dụng *(bắt buộc)*
- Các bước để tái hiện *(bắt buộc)*
- Tần suất *(bắt buộc)*
- Thiết bị/ROM *(tùy chọn)*
- Ảnh chụp màn hình / video *(nếu cần)*

-# ⚠️ Không dành cho lỗi đồng bộ hoặc cập nhật chương.
    """,

        "container3": """
    ## ❓ CÂU HỎI
- Tên: Câu hỏi
- Mô tả *(bắt buộc)*
- Phiên bản ứng dụng *(bắt buộc)*
- Ảnh chụp màn hình / video *(nếu cần)*
-# --> Vui lòng sử dụng cho việc đó https://discord.com/channels/1484655684879519885/1488486579872989294!

-# ⚠️ Chỉ dành cho câu hỏi về tính năng, không phải yêu cầu/đề xuất.
    """,

        "container4": """
## 🔄 LỖI ĐỒNG BỘ
- Tên: Lỗi đồng bộ hóa
- Mô tả *(bắt buộc)*
- Phiên bản ứng dụng *(bắt buộc)*
- Thiết bị/ROM *(bắt buộc)*
- Tần suất *(bắt buộc)*
- Ảnh chụp màn hình / video *(nếu cần)*
    """,

        "container5": """
## 📚 CẬP NHẬT CHƯƠNG
- Tên: Lỗi cập nhật chương
- Mô tả *(bắt buộc)*
- Phiên bản ứng dụng *(bắt buộc)*
- Tần suất xảy ra *(bắt buộc)*
- Ảnh chụp màn hình nhật ký cập nhật *(bắt buộc)*
- Minh chứng bổ sung *(nếu cần)*

### ⚠️ NOTES
-# - Chỉ hỗ trợ phiên bản mới nhất → https://discord.com/channels/1484655684879519885/1484655685542350991
-# - Chỉ sử dụng **một tag**
-# - Mẫu có thể thay đổi — luôn kiểm tra cập nhật
    """,
    },

}

class IssuesView(discord.ui.DesignerView):
    def __init__(self, lang: str = "en", show_buttons: bool = True):
        super().__init__(timeout=None)
        self.lang = ISSUES_LANGUAGES.get(
            lang,
            ISSUES_LANGUAGES["en"]
        )


        self.button_russia = discord.ui.Button(
            style=discord.ButtonStyle.grey,
            emoji="🇷🇺",
            custom_id="button_russia",
        )

        self.button_vietnam = discord.ui.Button(
            style=discord.ButtonStyle.grey,
            emoji="🇻🇳",
            custom_id="button_vietnam",
        )

        self.button_russia.callback = self.button_russia_callback
        self.button_vietnam.callback = self.button_vietnam_callback

        container1 = discord.ui.Container(
            discord.ui.Section(
            discord.ui.TextDisplay(
                content=self.lang["container1"]
            ),
            accessory=discord.ui.Thumbnail(url="https://cdn.discordapp.com/attachments/1487153908550729748/1508574348267491550/copy-paste-document-svgrepo-com1.png?ex=6a1608d8&is=6a14b758&hm=b8e56ff5721b30db8e0f315c491917048d2ae879e9a85e253e4a398f962b6a16&")
        )
    )

        container2 = discord.ui.Container(
            discord.ui.TextDisplay(
                content=self.lang["container2"]
            )
        )

        container3 = discord.ui.Container(
            discord.ui.TextDisplay(
                content=self.lang["container3"]
            )
        )

        container4 = discord.ui.Container(
            discord.ui.TextDisplay(
            content=self.lang["container4"]
        )
    )

        container5 = discord.ui.Container(
            discord.ui.TextDisplay(
            content=self.lang["container5"]
        )
    )

        self.add_item(container1)
        self.add_item(container2)
        self.add_item(container3)
        self.add_item(container4)
        self.add_item(container5)
        if show_buttons:
            self.add_item(
                discord.ui.ActionRow(
                    self.button_russia,
                    self.button_vietnam
                )
            )

    async def button_russia_callback(
            self,
            interaction: discord.Interaction
    ):
        await interaction.response.send_message(
            view=IssuesView(
                "ru",
                show_buttons=False
            ),
            ephemeral=True
        )

    async def button_vietnam_callback(
            self,
            interaction: discord.Interaction
    ):
        await interaction.response.send_message(
            view=IssuesView(
                "vi",
                show_buttons=False
            ),
            ephemeral=True
        )

class Texts(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._view_registered = False

    @commands.Cog.listener()
    async def on_ready(self):
        if not self._view_registered:
            self.bot.add_view(RolesView())
            self.bot.add_view(IssuesView())

            self._view_registered = True

    @slash_command()
    @commands.is_owner()
    async def panel(
            self,
            ctx: discord.ApplicationContext,
            panel: discord.Option(
                str,
                choices=[
                    "faq",
                    "rules",
                    "roles",
                    "issues",
                ]
            )
    ):

        await ctx.respond(
            "...",
            ephemeral=True
        )

        if panel == "faq":
            await ctx.channel.send(
                view=FAQView(),
                allowed_mentions=discord.AllowedMentions.none(),
            )

        elif panel == "rules":
            await ctx.channel.send(
                view=RulesView(),
                allowed_mentions=discord.AllowedMentions.none(),
            )
            await ctx.channel.send(
                """
-# Permanent Invite Link:
-# https://discord.gg/4AHskjwtj4
                """
            )

        elif panel == "roles":
            await ctx.channel.send(
                view=RolesView(),
                allowed_mentions=discord.AllowedMentions.none(),
            )

        elif panel == "issues":
            await ctx.channel.send(
                view=IssuesView(),
                allowed_mentions=discord.AllowedMentions.none(),
            )


def setup(bot):
    bot.add_cog(Texts(bot))
