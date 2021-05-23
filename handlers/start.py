from config import BOT_NAME as bot_username
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAEJlR9giNcPJke9BKSpQhP0zaOgf3z-KQACAQADFlyeOsyiWLhvkgt7HwQ")
    await message.reply_text(
        f"""⚜️<b>Hi {message.from_user.first_name}!⚜️

⚜️ I am PRINCE_MUSIC_BOT VC Music Player, an open-source bot that lets you play music in your Telegram groups.
Maintained by @Prince_3011 ❤

⚜️ For source code Join our support group @PRINCE_MUSIC_CHATS.

⚜️ Use the buttons below to know more about me.
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Command", url="https://t.me/PRINCEBOTS/4",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/PRINCEBOTSUPPORT"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/princebots"
                    ),
                    InlineKeyboardButton(
                        "😍 Credit", url="https://t.me/prince_3011"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📒TUTORIAL SCREENSHOT", url="https://t.me/joinchat/Ng0hJTU9SxcyNjdl"
                    ) 
                ]
            ]
        )
    )
@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/princebots"
                    )
                ],    
                [    
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("help")
    & filters.group
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!

⚜️Users Commands⚜️
/play <song name> - play song you requested
/dplay <song name> - play song you requested via deezer
/splay <song name> - play song you requested via jio saavn
/playlist - Show now playing list
/current - Show now playing
/song <song name> - download songs you want quickly
/search <query> - search videos on youtube with details
/deezer <song name> - download songs you want quickly via deezer
/saavn <song name> - download songs you want quickly via saavn
/video <song name> - download videos you want quickly

⚜️Admins only⚜️
/player - open Music player settings panel
/pause - pause song play
/resume - resume song play
/skip - play next song
/end - stop music play
/userbotjoin - invite assistant to your chat
/admincache - Refresh admin list
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/princebots"
                    )
                ]
            ]
        )
    )    
