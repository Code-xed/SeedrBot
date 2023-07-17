from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("support") | (filters.reply_keyboard & filters.regex(r"🎁 Support")))
async def support(_, message):
    text = '''
    🎁 Support

Thank you for your wish to contribute. Donate any amount to keep this service alive and to give me a motivation to add new features.😇

🐛 To report bugs or to request a new feature, join our discussion chat, and discuss it there.
    '''
    Buttons = [[InlineKeyboardButton("📢 Channel", url="https://t.me/H9YouTube"), InlineKeyboardButton("🗣️ Group Chat", url="https://t.me/+mxHaXtNFM1g5MzI1")], [InlineKeyboardButton("📺 YouTube", url="https://youtube.com/h9youtube"), InlineKeyboardButton("🧑‍💻 Follow on GitHub", url="https://github.com/hemantapkh")], [InlineKeyboardButton("☕ Donate", url="https://buymeacoffee.com/hemantapkh")]]
    IKB = InlineKeyboardMarkup(Buttons)
    await message.reply(text, reply_markup=IKB)
  
