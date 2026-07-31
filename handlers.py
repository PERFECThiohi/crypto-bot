import re

from telegram import Update
from telegram.ext import ContextTypes

from config import SUPPORTED_COINS
from prices import calculate_toman
from keyboards import buy_keyboard
from database import add_user
from logger import logger



# ==============================
# Persian Number Converter
# ==============================

def persian_to_english_numbers(text):

    numbers = {
        "۰": "0",
        "۱": "1",
        "۲": "2",
        "۳": "3",
        "۴": "4",
        "۵": "5",
        "۶": "6",
        "۷": "7",
        "۸": "8",
        "۹": "9"
    }

    for fa, en in numbers.items():
        text = text.replace(fa, en)

    return text



# ==============================
# Normalize Text
# ==============================

def normalize_text(text):

    text = persian_to_english_numbers(text)

    text = text.lower().strip()

    text = text.replace("‌", " ")

    return text



# ==============================
# Parse Input
# ==============================

def parse_input(text):

    text = normalize_text(text)


    # مثال:
    # 5 trx
    # ۵ ترون

    match = re.match(
        r"^(\d+(\.\d+)?)\s*(.+)$",
        text
    )


    if match:

        amount = float(
            match.group(1)
        )

        coin = match.group(3).strip()

        return amount, coin



    # فقط اسم ارز

    return 1, text



# ==============================
# Price Handler
# ==============================

async def price_handler(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):

    if not update.message:
        return


    user = update.effective_user


    await add_user(
        user.id,
        user.username,
        user.first_name
    )


    amount, coin = parse_input(
        update.message.text
    )


    if coin not in SUPPORTED_COINS:

        return



    symbol = SUPPORTED_COINS[coin]


    result = calculate_toman(
        symbol,
        amount
    )


    if result is None:

        await update.message.reply_text(
            "⚠️ خطا در دریافت قیمت. دوباره تلاش کنید."
        )

        return



    one_price = calculate_toman(
        symbol,
        1
    )


    message = (
    "🚀 Crypto Price\n\n"

    f"🪙 {coin.upper()}\n\n"

    "💵 قیمت فعلی\n"
    f"{result:,} تومان\n\n"

    "📌 وضعیت:\n"
    "🟢 Available\n\n"

    "━━━━━━━━━━━━━━\n\n"

    "🛍 خرید"
    
    )
    if amount != 1:

        message += (
            f"🔢 مقدار: {amount}\n"
            f"💵 ارزش کل:\n"
            f"{result:,} تومان"
        )


    await update.message.reply_text(
        message,
        reply_markup=buy_keyboard()
    )


    logger.info(
        f"{user.id} checked {coin}"
    )
    