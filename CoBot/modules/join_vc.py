from pyrogram import filters

from .. import BotMother, available_vc_clients
from ..utils.sudo_stat import sudo_only


@BotMother.on_message(filters.command("joinvc"))
@sudo_only
async def joiv_vc(bot, m):
    try:
        chat_id = int(m.text.split()[1])
        noofid = int(m.text.split()[2])
    except IndexError:
        return await m.reply("Give me chat id.")
    

@BotMother.on_message(filters.command("leavevc"))
@sudo_only
async def leave_vc(bot, m):
    try:
        chat_id = int(m.text.split()[1])
    except IndexError:
        return await m.reply("Give me chat id.")
    