from pyrogram import filters

from .. import BotFather, SUDO


@BotFather.on_message(filters.command("start"))
async def start(bot, m):
    if m.from_user.id not in SUDO:
        return await m.reply("I am a private bot, not intended for use by the general public.\n\n~ A bot by @CoderX")
    await m.reply("**Hola master!** \n\n    > how are you today? \nhow can I help you today!? know my commands /help\n\n~ A bot by @CoderX")