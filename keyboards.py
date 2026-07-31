from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from config import BUY_URL


# ==============================
# Buy Button
# ==============================

def buy_keyboard():
    """
    ساخت دکمه خرید ارز
    """

    keyboard = [
        [
            InlineKeyboardButton(
                text="🛒 خرید ارز",
                url=BUY_URL
            )
        ]
    ]

    return InlineKeyboardMarkup(keyboard)