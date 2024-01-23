import random
import asyncio

from pyrogram import filters


from .. import available_clients, LOGGER, BotFather
from ..utils.sudo_stat import sudo_only
from .database.main_db import Qspam



@BotFather.on_message(filters.command("qspam"))
@sudo_only
async def spamq(bot, m):
    chat_id = m.chat.id
    while True:
        for i in available_clients:
            xD = random.choice(open("questions.txt", "r").read())
            if i==1:
                ...
            else:
                await i.send_message(chat_id, xD)
                await asyncio.sleep(3)


@BotFather.on_message(filters.command("setspamstatus"))
@sudo_only
async def spamq(bot, m):
    chat_id = m.chat.id
    text = m.text[len("/setspamstatus ") :]
    if text == "on":
        status = 1
    else:
        status = 0
    await m.reply(Qspam.update_status(chat_id=chat_id, status=status))


@BotFather.on_message(filters.command("newspam"))
@sudo_only
async def newspam(bot, m):
    try:
        chat_id = m.text.split()[1]
    except IndexError:
        return await m.reply("Give me chat id")
    else:
        await m.reply(Qspam.insert(int(chat_id)))