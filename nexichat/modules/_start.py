import asyncio
import logging
import random
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pyrogram import Client, filters
from pyrogram.types import Message
from nexichat import nexichat
from nexichat.database.chats import get_served_chats
from nexichat.database.users import get_served_users
from config import OWNER_ID
from nexichat import nexichat
import asyncio
import logging
from pyrogram import filters
from pyrogram.errors import FloodWait
from nexichat import nexichat
from nexichat.database.chats import get_served_chats
from nexichat.database.users import get_served_users
from nexichat.database.chats import add_served_chat
from nexichat.database.users import add_served_user
from nexichat.modules.helpers import (
    CLOSE_BTN,
    HELP_BTN,
    HELP_BUTN,
    HELP_READ,
    HELP_START,
    SOURCE_READ,
    START,
)

STICKER = [
    "CAACAgUAAx0CYlaJawABBy4vZaieO6T-Ayg3mD-JP-f0yxJngIkAAv0JAALVS_FWQY7kbQSaI-geBA",
    "CAACAgUAAx0CYlaJawABBy4rZaid77Tf70SV_CfjmbMgdJyVD8sAApwLAALGXCFXmCx8ZC5nlfQeBA",
    "CAACAgUAAx0CYlaJawABBy4jZaidvIXNPYnpAjNnKgzaHmh3cvoAAiwIAAIda2lVNdNI2QABHuVVHgQ",
]


EMOJIOS = [
    "💣",
    "💥",
    "🪄",
    "🧨",
    "⚡",
    "🤡",
    "👻",
    "🎃",
    "🎩",
    "🕊",
]

IMG = [
    "https://graph.org/file/210751796ff48991b86a3.jpg",
    "https://graph.org/file/7b4924be4179f70abcf33.jpg",
    "https://graph.org/file/f6d8e64246bddc26b4f66.jpg",
    "https://graph.org/file/63d3ec1ca2c965d6ef210.jpg",
    "https://graph.org/file/9f12dc2a668d40875deb5.jpg",
    "https://graph.org/file/0f89cd8d55fd9bb5130e1.jpg",
    "https://graph.org/file/e5eb7673737ada9679b47.jpg",
    "https://graph.org/file/2e4dfe1fa5185c7ff1bfd.jpg",
    "https://graph.org/file/36af423228372b8899f20.jpg",
    "https://graph.org/file/c698fa9b221772c2a4f3a.jpg",
    "https://graph.org/file/61b08f41855afd9bed0ab.jpg",
    "https://graph.org/file/744b1a83aac76cb3779eb.jpg",
    "https://graph.org/file/814cd9a25dd78480d0ce1.jpg",
    "https://graph.org/file/e8b472bcfa6680f6c6a5d.jpg",
]



languages = {
    # Top 20 languages used on Telegram
    'english': 'en', 'hindi': 'hi', 'Myanmar': 'my', 'russian': 'ru', 'spanish': 'es', 
    'arabic': 'ar', 'turkish': 'tr', 'german': 'de', 'french': 'fr', 
    'italian': 'it', 'persian': 'fa', 'indonesian': 'id', 'portuguese': 'pt',
    'ukrainian': 'uk', 'filipino': 'tl', 'korean': 'ko', 'japanese': 'ja', 
    'polish': 'pl', 'vietnamese': 'vi', 'thai': 'th', 'dutch': 'nl',

    # Top languages spoken in Bihar
    'bhojpuri': 'bho', 'maithili': 'mai', 'urdu': 'ur', 
    'bengali': 'bn', 'magahi': 'mag', 'angika': 'anp', 'sanskrit': 'sa', 
    'oriya': 'or', 'nepali': 'ne', 'santhali': 'sat', 'khortha': 'kht', 
    'kurmali': 'kyu', 'ho': 'hoc', 'munda': 'unr', 'kharwar': 'kqw', 
    'mundari': 'unr', 'sadri': 'sck', 'pali': 'pi', 'tamil': 'ta',

    # Top languages spoken in India
    'telugu': 'te', 'bengali': 'bn', 'marathi': 'mr', 'tamil': 'ta', 
    'gujarati': 'gu', 'urdu': 'ur', 'kannada': 'kn', 'malayalam': 'ml', 
    'odia': 'or', 'punjabi': 'pa', 'assamese': 'as', 'sanskrit': 'sa', 
    'kashmiri': 'ks', 'konkani': 'gom', 'sindhi': 'sd', 'bodo': 'brx', 
    'dogri': 'doi', 'santali': 'sat', 'meitei': 'mni', 'nepali': 'ne',

    # Other language
    'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'armenian': 'hy', 
    'aymara': 'ay', 'azerbaijani': 'az', 'bambara': 'bm', 
    'basque': 'eu', 'belarusian': 'be', 'bosnian': 'bs', 'bulgarian': 'bg', 
    'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 
    'chinese (simplified)': 'zh-CN', 'chinese (traditional)': 'zh-TW', 
    'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 
    'dhivehi': 'dv', 'esperanto': 'eo', 'estonian': 'et', 'ewe': 'ee', 
    'finnish': 'fi', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 
    'greek': 'el', 'guarani': 'gn', 'haitian creole': 'ht', 'hausa': 'ha', 
    'hawaiian': 'haw', 'hebrew': 'iw', 'hmong': 'hmn', 'hungarian': 'hu', 
    'icelandic': 'is', 'igbo': 'ig', 'ilocano': 'ilo', 'irish': 'ga', 
    'javanese': 'jw', 'kazakh': 'kk', 'khmer': 'km', 'kinyarwanda': 'rw', 
    'krio': 'kri', 'kurdish (kurmanji)': 'ku', 'kurdish (sorani)': 'ckb', 
    'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 
    'lingala': 'ln', 'lithuanian': 'lt', 'luganda': 'lg', 'luxembourgish': 'lb', 
    'macedonian': 'mk', 'malagasy': 'mg', 'maltese': 'mt', 'maori': 'mi', 
    'mizo': 'lus', 'mongolian': 'mn', 'myanmar': 'my', 'norwegian': 'no', 
    'oromo': 'om', 'pashto': 'ps', 'quechua': 'qu', 'romanian': 'ro', 
    'samoan': 'sm', 'scots gaelic': 'gd', 'sepedi': 'nso', 'serbian': 'sr', 
    'sesotho': 'st', 'shona': 'sn', 'sinhala': 'si', 'slovak': 'sk', 
    'slovenian': 'sl', 'somali': 'so', 'sundanese': 'su', 'swahili': 'sw', 
    'swedish': 'sv', 'tajik': 'tg', 'tatar': 'tt', 'tigrinya': 'ti', 
    'tsonga': 'ts', 'turkmen': 'tk', 'twi': 'ak', 'uyghur': 'ug', 
    'uzbek': 'uz', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 
    'yoruba': 'yo', 'zulu': 'zu'
}

def generate_language_buttons(page=1):
    buttons = []
    items_per_page = 10
    lang_items = list(languages.items())
    
    start_index = (page - 1) * items_per_page
    end_index = start_index + items_per_page

    for i in range(start_index, min(end_index, len(lang_items)), 2):
        row = []
        for j in range(i, min(i + 2, end_index)):  # 2 buttons per row
            lang_name, lang_code = lang_items[j]
            row.append(InlineKeyboardButton(lang_name.title(), callback_data=f"setlang_{lang_code}"))
        buttons.append(row)

    nav_buttons = []
    if page > 1:
        nav_buttons.append(InlineKeyboardButton("Back", callback_data=f"language_page_{page - 1}"))
    if end_index < len(lang_items):
        nav_buttons.append(InlineKeyboardButton("Next", callback_data=f"language_page_{page + 1}"))

    if nav_buttons:
        buttons.append(nav_buttons)

    return buttons

@nexichat.on_message(filters.command(["lang", "language", "setlang"]))
async def set_language(client: Client, message: Message):
    await message.reply_text(
        "ᴘʟᴇᴀsᴇ sᴇʟᴇᴄᴛ ʏᴏᴜʀ ᴄʜᴀᴛ ʟᴀɴɢᴜᴀɢᴇ:",
        reply_markup=InlineKeyboardMarkup(generate_language_buttons())
    )


@nexichat.on_message(filters.new_chat_members)
async def welcomejej(client, message: Message):
    await add_served_chat(message.chat.id)
    try:
        for member in message.new_chat_members:
            await message.reply_photo(photo=random.choice(IMG), caption=START, reply_markup=InlineKeyboardMarkup(generate_language_buttons()))
            
            chat = message.chat   
            
            if member.id == nexichat.id:
                try:
                    invitelink = await nexichat.export_chat_invite_link(message.chat.id)
                    link = f"[ɢᴇᴛ ʟɪɴᴋ]({invitelink})"
                except ChatAdminRequired:
                    link = "No Link"
                    
                try:
                    groups_photo = await nexichat.download_media(
                        chat.photo.big_file_id, file_name=f"chatpp{chat.id}.png"
                    )
                    chat_photo = (
                        groups_photo if groups_photo else "https://envs.sh/IL_.jpg"
                    )
                except AttributeError:
                    chat_photo = "https://envs.sh/IL_.jpg"
                
                count = await nexichat.get_chat_members_count(chat.id)
                username = chat.username if chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐆ʀᴏᴜᴘ"
                msg = (
                    f"**📝𝐌ᴜsɪᴄ 𝐁ᴏᴛ 𝐀ᴅᴅᴇᴅ 𝐈ɴ 𝐀 #𝐍ᴇᴡ_𝐆ʀᴏᴜᴘ**\n\n"
                    f"**📌𝐂ʜᴀᴛ 𝐍ᴀᴍᴇ:** {chat.title}\n"
                    f"**🍂𝐂ʜᴀᴛ 𝐈ᴅ:** `{chat.id}`\n"
                    f"**🔐𝐂ʜᴀᴛ 𝐔sᴇʀɴᴀᴍᴇ:** @{username}\n"
                    f"**🖇️𝐆ʀᴏᴜᴘ 𝐋ɪɴᴋ:** {link}\n"
                    f"**📈𝐆ʀᴏᴜᴘ 𝐌ᴇᴍʙᴇʀs:** {count}\n"
                    f"**🤔𝐀ᴅᴅᴇᴅ 𝐁ʏ:** {message.from_user.mention}"
                )

                try:
                    owner_username = True
                    loggin.info(message.from_user.id)
                    if owner_username:
                        await nexichat.send_photo(
                            int(OWNER_ID),
                            photo=chat_photo,
                            caption=msg,
                            reply_markup=InlineKeyboardMarkup(
                                [
                                    [
                                        InlineKeyboardButton(
                                            f"😍𝐀ᴅᴅᴇᴅ 𝐁ʏ😍",
                                            url=f"tg://openmessage?user_id={message.from_user.id}",
                                        )
                                    ]
                                ]
                            ),
                        )
                    else:
                        await nexichat.send_photo(
                            int(OWNER_ID),
                            photo=chat_photo,
                            caption=msg,
                            reply_markup=InlineKeyboardMarkup(
                                [
                                    [
                                        InlineKeyboardButton(
                                            f"😍𝐀ᴅᴅᴇᴅ 𝐁ʏ😍",
                                            url=f"tg://openmessage?user_id={message.from_user.id}",
                                        )
                                    ]
                                ]
                            ),
                        )
                except Exception as e:
                    logging.info(f"Error fetching owner username: {e}")
                    await nexichat.send_photo(
                        int(OWNER_ID),
                        photo=chat_photo,
                        caption=msg,
                        reply_markup=InlineKeyboardMarkup(
                            [
                                [
                                    InlineKeyboardButton(
                                        f"😍𝐀ᴅᴅᴇᴅ 𝐁ʏ😍",
                                        url=f"tg://openmessage?user_id={message.from_user.id}",
                                    )
                                ]
                            ]
                        ),
                    )

    except Exception as e:
        logging.info(f"Error: {e}")


@nexichat.on_cmd(["start", "aistart"])
async def start(_, m: Message):
    if m.chat.type == ChatType.PRIVATE:
        accha = await m.reply_text(
            text=random.choice(EMOJIOS),
        )
        await asyncio.sleep(1.3)
        await accha.edit("__ᴅιиg ᴅσиg ꨄ︎ ѕтαятιиg..__")
        await asyncio.sleep(0.2)
        await accha.edit("__ᴅιиg ᴅσиg ꨄ sтαятιиg.....__")
        await asyncio.sleep(0.2)
        await accha.edit("__ᴅιиg ᴅσиg ꨄ︎ sтαятιиg..__")
        await asyncio.sleep(0.2)
        await accha.delete()
        umm = await m.reply_sticker(sticker=random.choice(STICKER))
        await asyncio.sleep(2)
        await umm.delete()
        await m.reply_text(text=f"""**๏ ʜᴇʏ..**\n\n**🥀ʜᴏᴡ ᴀʀᴇ ʏᴏᴜ ʙᴀʙʏ...?**""")
        await add_served_user(m.chat.id)
    else:
        await m.reply_photo(
            photo=random.choice(IMG),
            caption=START,
            reply_markup=InlineKeyboardMarkup(HELP_START),
        )
        await add_served_chat(m.chat.id)


@nexichat.on_cmd("help")
async def help(client: nexichat, m: Message):
    if m.chat.type == ChatType.PRIVATE:
        hmm = await m.reply_photo(
            photo=random.choice(IMG),
            caption=HELP_READ,
            reply_markup=InlineKeyboardMarkup(HELP_BTN),
        )

    else:
        await m.reply_photo(
            photo=random.choice(IMG),
            caption="**ʜᴇʏ, ᴘᴍ ᴍᴇ ғᴏʀ ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅs!**",
            reply_markup=InlineKeyboardMarkup(HELP_BUTN),
        )
        await add_served_chat(m.chat.id)


@nexichat.on_cmd("repo")
async def repo(_, m: Message):
    await m.reply_text(
        text=SOURCE_READ,
        reply_markup=InlineKeyboardMarkup(CLOSE_BTN),
        disable_web_page_preview=True,
    )


import random
from datetime import datetime

from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message

from config import OWNER_USERNAME
from nexichat import nexichat
from nexichat.database.chats import add_served_chat
from nexichat.database.users import add_served_user
from nexichat.modules.helpers import PNG_BTN

IMG = [
    "https://graph.org/file/210751796ff48991b86a3.jpg",
    "https://graph.org/file/7b4924be4179f70abcf33.jpg",
    "https://graph.org/file/f6d8e64246bddc26b4f66.jpg",
    "https://graph.org/file/63d3ec1ca2c965d6ef210.jpg",
    "https://graph.org/file/9f12dc2a668d40875deb5.jpg",
    "https://graph.org/file/0f89cd8d55fd9bb5130e1.jpg",
    "https://graph.org/file/e5eb7673737ada9679b47.jpg",
    "https://graph.org/file/2e4dfe1fa5185c7ff1bfd.jpg",
    "https://graph.org/file/36af423228372b8899f20.jpg",
    "https://graph.org/file/c698fa9b221772c2a4f3a.jpg",
    "https://graph.org/file/61b08f41855afd9bed0ab.jpg",
    "https://graph.org/file/744b1a83aac76cb3779eb.jpg",
    "https://graph.org/file/814cd9a25dd78480d0ce1.jpg",
    "https://graph.org/file/e8b472bcfa6680f6c6a5d.jpg",
]


STICKER = [
    "CAACAgUAAx0CYlaJawABBy4vZaieO6T-Ayg3mD-JP-f0yxJngIkAAv0JAALVS_FWQY7kbQSaI-geBA",
    "CAACAgUAAx0CYlaJawABBy4rZaid77Tf70SV_CfjmbMgdJyVD8sAApwLAALGXCFXmCx8ZC5nlfQeBA",
    "CAACAgUAAx0CYlaJawABBy4jZaidvIXNPYnpAjNnKgzaHmh3cvoAAiwIAAIda2lVNdNI2QABHuVVHgQ",
]


@nexichat.on_cmd("ping")
async def ping(_, message: Message):
    start = datetime.now()
    loda = await message.reply_photo(
        photo=random.choice(IMG),
        caption="ᴘɪɴɢɪɴɢ...",
    )

    ms = (datetime.now() - start).microseconds / 1000
    await loda.edit_text(
        text=f"нey вαву!!\n{nexichat.name} ᴄʜᴀᴛʙᴏᴛ ιѕ alιve 🥀 αnd worĸιng ғιne wιтн a pιng oғ\n➥ `{ms}` ms\n\n<b>|| мαdє ωιтн ❣️ ву [ᴠɪᴘ ʙᴏʏ](https://t.me/{OWNER_USERNAME}) ||</b>",
        reply_markup=InlineKeyboardMarkup(PNG_BTN),
    )
    if message.chat.type == ChatType.PRIVATE:
        await add_served_user(message.from_user.id)
    else:
        await add_served_chat(message.chat.id)


@nexichat.on_message(filters.command("stats"))
async def stats(cli: Client, message: Message):
    users = len(await get_served_users())
    chats = len(await get_served_chats())
    await message.reply_text(
        f"""{(await cli.get_me()).mention} ᴄʜᴀᴛʙᴏᴛ sᴛᴀᴛs:

➻ **ᴄʜᴀᴛs :** {chats}
➻ **ᴜsᴇʀs :** {users}"""
    )


from pyrogram.enums import ParseMode

from nexichat import nexichat


@nexichat.on_cmd("id")
async def getid(client, message):
    chat = message.chat
    your_id = message.from_user.id
    message_id = message.id
    reply = message.reply_to_message

    text = f"**[ᴍᴇssᴀɢᴇ ɪᴅ:]({message.link})** `{message_id}`\n"
    text += f"**[ʏᴏᴜʀ ɪᴅ:](tg://user?id={your_id})** `{your_id}`\n"

    if not message.command:
        message.command = message.text.split()

    if not message.command:
        message.command = message.text.split()

    if len(message.command) == 2:
        try:
            split = message.text.split(None, 1)[1].strip()
            user_id = (await client.get_users(split)).id
            text += f"**[ᴜsᴇʀ ɪᴅ:](tg://user?id={user_id})** `{user_id}`\n"

        except Exception:
            return await message.reply_text("ᴛʜɪs ᴜsᴇʀ ᴅᴏᴇsɴ'ᴛ ᴇxɪsᴛ.", quote=True)

    text += f"**[ᴄʜᴀᴛ ɪᴅ:](https://t.me/{chat.username})** `{chat.id}`\n\n"

    if (
        not getattr(reply, "empty", True)
        and not message.forward_from_chat
        and not reply.sender_chat
    ):
        text += f"**[ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇ ɪᴅ:]({reply.link})** `{reply.id}`\n"
        text += f"**[ʀᴇᴘʟɪᴇᴅ ᴜsᴇʀ ɪᴅ:](tg://user?id={reply.from_user.id})** `{reply.from_user.id}`\n\n"

    if reply and reply.forward_from_chat:
        text += f"ᴛʜᴇ ғᴏʀᴡᴀʀᴅᴇᴅ ᴄʜᴀɴɴᴇʟ, {reply.forward_from_chat.title}, ʜᴀs ᴀɴ ɪᴅ ᴏғ `{reply.forward_from_chat.id}`\n\n"
        print(reply.forward_from_chat)

    if reply and reply.sender_chat:
        text += f"ɪᴅ ᴏғ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴄʜᴀᴛ/ᴄʜᴀɴɴᴇʟ, ɪs `{reply.sender_chat.id}`"
        print(reply.sender_chat)

    await message.reply_text(
        text,
        disable_web_page_preview=True,
        parse_mode=ParseMode.DEFAULT,
    )


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

AUTO_SLEEP = 5
IS_BROADCASTING = False
broadcast_lock = asyncio.Lock()


@nexichat.on_message(
    filters.command(["broadcast", "gcast"]) & filters.user(int(OWNER_ID))
)
async def broadcast_message(client, message):
    global IS_BROADCASTING
    async with broadcast_lock:
        if IS_BROADCASTING:
            return await message.reply_text(
                "A broadcast is already in progress. Please wait for it to complete."
            )

        IS_BROADCASTING = True
        try:
            query = message.text.split(None, 1)[1].strip()
        except IndexError:
            query = message.text.strip()
        except Exception as eff:
            return await message.reply_text(
                f"**Error**: {eff}"
            )
        try:
            if message.reply_to_message:
                broadcast_content = message.reply_to_message
                broadcast_type = "reply"
                flags = {
                    "-pin": "-pin" in query,
                    "-pinloud": "-pinloud" in query,
                    "-nogroup": "-nogroup" in query,
                    "-user": "-user" in query,
                }
            else:
                if len(message.command) < 2:
                    return await message.reply_text(
                        "**Please provide text after the command or reply to a message for broadcasting.**"
                    )
                
                flags = {
                    "-pin": "-pin" in query,
                    "-pinloud": "-pinloud" in query,
                    "-nogroup": "-nogroup" in query,
                    "-user": "-user" in query,
                }

                for flag in flags:
                    query = query.replace(flag, "").strip()

                if not query:
                    return await message.reply_text(
                        "Please provide a valid text message or a flag: -pin, -nogroup, -pinloud, -user"
                    )

                
                broadcast_content = query
                broadcast_type = "text"
            

            await message.reply_text("**Started broadcasting...**")

            if not flags.get("-nogroup", False):
                sent = 0
                pin_count = 0
                chats = await get_served_chats()

                for chat in chats:
                    chat_id = int(chat["chat_id"])
                    if chat_id == message.chat.id:
                        continue
                    try:
                        if broadcast_type == "reply":
                            m = await nexichat.forward_messages(
                                chat_id, message.chat.id, [broadcast_content.id]
                            )
                        else:
                            m = await nexichat.send_message(
                                chat_id, text=broadcast_content
                            )
                        sent += 1

                        if flags.get("-pin", False) or flags.get("-pinloud", False):
                            try:
                                await m.pin(
                                    disable_notification=flags.get("-pin", False)
                                )
                                pin_count += 1
                            except Exception as e:
                                logger.error(
                                    f"Failed to pin message in chat {chat_id}: {e}"
                                )

                    except FloodWait as e:
                        flood_time = int(e.value)
                        logger.warning(
                            f"FloodWait of {flood_time} seconds encountered for chat {chat_id}."
                        )
                        if flood_time > 200:
                            logger.info(
                                f"Skipping chat {chat_id} due to excessive FloodWait."
                            )
                            continue
                        await asyncio.sleep(flood_time)
                    except Exception as e:
                        logger.error(f"Error broadcasting to chat {chat_id}: {e}")
                        continue

                await message.reply_text(
                    f"**Broadcasted to {sent} chats and pinned in {pin_count} chats.**"
                )

            if flags.get("-user", False):
                susr = 0
                users = await get_served_users()

                for user in users:
                    user_id = int(user["user_id"])
                    try:
                        if broadcast_type == "reply":
                            m = await nexichat.forward_messages(
                                user_id, message.chat.id, [broadcast_content.id]
                            )
                        else:
                            m = await nexichat.send_message(
                                user_id, text=broadcast_content
                            )
                        susr += 1

                    except FloodWait as e:
                        flood_time = int(e.value)
                        logger.warning(
                            f"FloodWait of {flood_time} seconds encountered for user {user_id}."
                        )
                        if flood_time > 200:
                            logger.info(
                                f"Skipping user {user_id} due to excessive FloodWait."
                            )
                            continue
                        await asyncio.sleep(flood_time)
                    except Exception as e:
                        logger.error(f"Error broadcasting to user {user_id}: {e}")
                        continue

                await message.reply_text(f"**Broadcasted to {susr} users.**")

        finally:
            IS_BROADCASTING = False
