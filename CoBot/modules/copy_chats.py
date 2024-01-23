import random

from pyrogram import Client, filters


from .. import available_clients, LOGGER, BotFather, BotMother
from ..utils.sudo_stat import sudo_only
from .database.main_db import Chats, OnStatus, Last





@BotFather.on_message(filters.command("status"))
@sudo_only
async def status_update(bot, m):
    try:
        chat_id = int(m.text.split()[2])
        text = m.text.split()[1]
    except:
        return await m.reply("Invalid chat id!")
    command = text.lower()
    if command not in ["on", "off"]:
        return await m.reply("Invalid status, try: on, off")
    else:
        if command == "on":
            status = 1
        else:
            status = 0
        OnStatus.update_status(chat_id, status)
        await m.reply(f"Status changed to {command} for {chat_id}")


@BotFather.on_message(filters.command("newchat"))
@sudo_only
async def new_chat_target(bot, m):
    try:
        target_chat_id = int(m.text.split()[1])
        chat_id = int(m.text.split()[2])
    except IndexError:
        return await m.reply("Kindly give me chat_id")
    OnStatus.update_status(chat_id, 1)
    chats = eval(Chats().get_chats())
    chats[chat_id]=target_chat_id
    await m.reply(Chats().update(str(chats)))


@BotFather.on_message(filters.command("delchat"))
@sudo_only
async def del_chat(bot, m):
    try:
        chat_id = int(m.text.split()[1])
    except IndexError:
        return await m.reply("Kindly give me chat_id")
    Chats().delete(chat_id)
    await m.reply(f"Deleted {chat_id}")


@BotFather.on_message(filters.command("joinchat"))
@sudo_only
async def joinchat(bot, m):
    uname = m.text.split()[1]
    await BotMother.join_chat(uname)
    for i in available_clients:
        await i.join_chat(uname)
    await m.reply("Joined successfully.")