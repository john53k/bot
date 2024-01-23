import loguru

from pyrogram import Client

from config import *




LOGGER = loguru.logger
BotMother = Client(
    "BotMother",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=MOTHERSESSION,
    )

DbSaver = Client(
    "Saver",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=DATASAVER
)

BotFather = Client(
    "BotFather",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=TOKEN,
    plugins={"root":"CoBot.modules"}
    )

available_clients = []
