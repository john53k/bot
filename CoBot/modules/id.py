from pyrogram import filters

from .. import BotFather




@BotFather.on_message(filters.command("id"))
async def status_update(bot, m):
    try:
        await m.reply(f"> Your id: `{m.from_user.id}`\n> Chat id: `{m.chat.id}`")
    except:
        ...