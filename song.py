from pyrogram.types import InlineKeyboardButton
from Bikash import config

def song_markup(_, vidid):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["SG_B_2"],
                callback_data=f"song_helper audio|{vidid}",
            ),
            InlineKeyboardButton(
                text=_["SG_B_3"],
                callback_data=f"song_helper video|{vidid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data="close"
            ),
        ],
        [
            InlineKeyboardButton(
                text="🌷 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 🌷", url=f"{sarkar.config.SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text="𝐔𝐩𝐝𝐚𝐭𝐞𝐬", url=f"https://t.me/TKS_CHAT_OFFICIAL"
            ),
        ],
    ]
    return buttons
