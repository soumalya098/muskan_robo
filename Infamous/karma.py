# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX
# https://t.me/O_okarma

# <============================================== IMPORTS =========================================================>
from pyrogram.types import InlineKeyboardButton as ib
from telegram import InlineKeyboardButton

from Mikobot import BOT_USERNAME, OWNER_ID, SUPPORT_CHAT

# <============================================== CONSTANTS =========================================================>
START_IMG = [
    "https://telegra.ph/file/51a0263465798bf6b04cf.jpg",
    "https://telegra.ph/file/51a0263465798bf6b04cf.jpg",
    "https://telegra.ph/file/51a0263465798bf6b04cf.jpg",
    "https://telegra.ph/file/51a0263465798bf6b04cf.jpg",
    "https://telegra.ph/file/51a0263465798bf6b04cf.jpg",
    "https://telegra.ph/file/51a0263465798bf6b04cf.jpg",
    "https://telegra.ph/file/51a0263465798bf6b04cf.jpg",
]

HEY_IMG = "https://te.legra.ph/file/8c4b7ef12ee1445ad3276.jpg"

ALIVE_ANIMATION = [
    "https://telegra.ph//file/f9e2b9cdd9324fc39970a.mp4",
    "https://telegra.ph//file/8d4d7d06efebe2f8becd0.mp4",
    "https://telegra.ph//file/c4c2759c5fc04cefd207a.mp4",
    "https://telegra.ph//file/b1fa6609b1c4807255927.mp4",
    "https://telegra.ph//file/f3c7147da6511fbe27c25.mp4",
    "https://telegra.ph//file/39071b73c02e3ff5945ca.mp4",
    "https://telegra.ph//file/8d4d7d06efebe2f8becd0.mp4",
    "https://telegra.ph//file/6efdd8e28756bc2f6e53e.mp4",
]

BAN_GIFS = [
    "https://te.legra.ph/file/ea0f7581cfd3c09645fca.mp4",
]


KICK_GIFS = [
    "https://te.legra.ph/file/2eca660c64dd64e2400e7.mp4",
]


MUTE_GIFS = [
    "https://te.legra.ph/file/ee2a903707ed78a37f70a.mp4",
]

FIRST_PART_TEXT = "✨ *ʙᴜᴅᴅʏ🪄✨* `{}` . . ."

PM_START_TEXT = "✨ *ɪ ᴀᴍ Muskan Robo, ᴀ ɢᴇɴꜱʜɪɴ ɪᴍᴘᴀᴄᴛ ᴛʜᴇᴍᴇᴅ ʀᴏʙᴏᴛ ᴡʜɪᴄʜ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ᴍᴀɴᴀɢᴇ ᴀɴᴅ ꜱᴇᴄᴜʀᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴡɪᴛʜ ʜᴜɢᴇ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ*"

START_BTN = [
    [
        InlineKeyboardButton(
            text="✨sᴜᴍᴍᴏɴ ᴍᴇ✨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="🪄ᴄᴏᴍᴍᴀɴᴅs🪄", callback_data="help_back"),
    ],
    [
        InlineKeyboardButton(text="▫️ᴀʙᴏᴜᴛ▫️", callback_data="Miko_"),
        InlineKeyboardButton(text="🔹ᴀɪ ʀᴏʙᴏ🔹", callback_data="ai_handler"),
        InlineKeyboardButton(text="⚡REPO⚡", callback_data="git_source"),
    ],
    [
        InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇs", url=f"https://t.me/Muskan_music_2_bot"),
    ],
]

GROUP_START_BTN = [
    [
        InlineKeyboardButton(
            text="ᴀᴅᴅ ᴍᴇ ᴅᴀʀʟᴏ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="✨ʜᴏᴜsᴇ✨", url=f"https://t.me/{SUPPORT_CHAT}"),
        InlineKeyboardButton(text="⚡ᴅᴇᴠ⚡", url=f"tg://user?id={OWNER_ID}"),
    ],
]

ALIVE_BTN = [
    [
        ib(text="UPDATES", url="https://t.me/galaxy_chatting_group"),
        ib(text="SUPPORT", url="https://t.me/galaxy_chatting_group"),
    ],
    [
        ib(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

HELP_STRINGS = """
🫧 *Muskan Robo* 🫧

☉ * ʜ⚡ᴇʏᴀ ᴀʟʟ MUSKAN ROBO ᴄᴏᴍᴍᴀɴᴅ ʟɪsᴛ ʜᴇʀᴇ ʀᴇᴀᴅ ᴄᴀʀᴇғᴜʟʟʏ ⚡.*

ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /
"""
