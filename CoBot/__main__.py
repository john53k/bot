import os
import random
import asyncio


from pyrogram import idle

from . import *





async def main():
    from .modules.database.main_db import Session
    STRING_SESSIONS1 = STRING_SESSIONS
    for i in Session.get():
        LOGGER.info(i)
        STRING_SESSIONS1.append(i[0])
    try:
        LOGGER.info("Starting bot father")
        await BotFather.start()
    except Exception as e: 
        LOGGER.error(e)
        exit("Exitting...")
    else:
        LOGGER.info("Started Bot father")
    try:
        LOGGER.info("Starting bot mother...")
        await BotMother.start()
    except Exception as e:
        LOGGER.error(e)
        exit()
    else:
        LOGGER.info("Started bot mother...")

    try:
        LOGGER.info("Starting db saver...")
        await DbSaver.start()
    except Exception as e:
        LOGGER.error(e)
        exit()
    else:
        LOGGER.info("Started db saver...")
    LOGGER.info("Getting sessions....")
    cno = 1
    for i in STRING_SESSIONS1:
        copy_ninja_kakashi = Client(
                f"Copy",
                api_id=API_ID,
                api_hash=API_HASH,
                session_string=i,
            )
        try:
            await copy_ninja_kakashi.start()
        except Exception as e:
            LOGGER.error(e)
        else:
            LOGGER.info(f"Number {cno} child has born, Oh! I mean {cno} Client has started...")
            available_clients.append(copy_ninja_kakashi)
            cno+=1
    LOGGER.info(f"{len(available_clients)} started!")

    await idle()
    LOGGER.info("Sopping all clients...")
    for i in available_clients:
        await i.stop()
    LOGGER.info("Bot stopped Alvida!")

BotFather.run(main())
