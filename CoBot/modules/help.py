from pyrogram import Client, filters

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from .. import BotFather
from ..utils.sudo_stat import sudo_only



modules = {
    "Status 🔍":"/status chat_id on/off : Change copying status✨",
    "New Chat 🆕":"/newchat chat_id target_chat_id : Set new chat and target chat",
    "🗑️ Delete chat 🗑️":"/delchat ᴄʜᴀᴛ_ɪᴅ: Delete chat",
    "Join chat 🤞":"/joinchat chat_username : Join a chat.",
    "Join Vc ➿":"/joinvc chat_id number_of_accounts_to_join_with.: Join voice chat",
    "Online 💫":"/online : Accounts will come online.",
    "Offline ❌":"/offline : Accounts will go offline.",
    "Question spam":"""/newspam chat_id : Set chat id to spam questions\n/qspam : Start spamming\n/setspamstatus on/off : Set spam status"""
}

@BotFather.on_message(filters.command("help"))
@sudo_only
async def help(bot, m):
    btn = []
    count = 1
    cr = 0
    for i in modules.keys():
        btn[count].append(InlineKeyboardButton(i, callback_data=f"help_{i}"))
        count+=1
        
    await m.reply_photo(photo="https://graph.org/file/d60dbbf2caffa229915e9.jpg", caption="I ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴡɪᴛʜ:", reply_markup=InlineKeyboardMarkup(btn))



@Client.on_callback_query(filters.regex(r"^help_"))
async def help_callback(bot, q):
    back = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("ʙᴀᴄᴋ", callback_data = "helpback")
            ]
        ]
    )
    data = q.data.split("_")[1]
    txt = f"🍀 Hᴇʟᴘ ғᴏʀ {data} ᴍᴏᴅᴜʟᴇ 🍀\n\n"
    await q.message.edit_text(txt+modules[data], reply_markup=back)


@Client.on_callback_query(filters.regex(r"^helpback"))
async def help_callbacl_back(bot, q: CallbackQuery):
    exit()