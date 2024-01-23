from pyrogram import filters


from .. import available_clients, BotFather, BotMother, LOGGER
from ..utils.sudo_stat import sudo_only



@BotFather.on_message(filters.command("online"))
@sudo_only
async def online(bot, m):
    for i in available_clients:
        y = await i.invoke(offline=False)
        LOGGER.info(y)
    X = await BotMother.invoke(offline=False)
    LOGGER.info(X)
    await m.reply("Yep")

@BotFather.on_message(filters.command("offline"))
@sudo_only
async def offline(bot, m):
    for i in available_clients:
        await i.invoke(offline=True)
    await BotMother.invoke(offline=True)
    await m.reply("Executed")
