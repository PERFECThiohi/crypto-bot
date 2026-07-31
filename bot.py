from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

from config import BOT_TOKEN
from handlers import price_handler
from database import init_db
from logger import logger


# ==============================
# Start Command
# ==============================

async def start_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    if update.message:

        await update.message.reply_text(
            "🤖 ربات قیمت ارز فعال شد.\n\n"
            "برای دریافت قیمت ارسال کنید:\n\n"
            "مثال:\n"
            "trx\n"
            "5 trx\n"
            "0.2 btc"
        )


# ==============================
# Application Startup
# ==============================

async def on_startup(
    application: Application
):

    try:

        await init_db()

        logger.info(
            "Database initialized successfully"
        )

    except Exception as e:

        logger.error(
            f"Database error: {e}"
        )

        raise e



# ==============================
# Main
# ==============================

def main():

    if not BOT_TOKEN:

        raise ValueError(
            "BOT_TOKEN is missing!"
        )


    app = (
        Application
        .builder()
        .token(BOT_TOKEN)
        .post_init(on_startup)
        .build()
    )


    # /start

    app.add_handler(
        CommandHandler(
            "start",
            start_command
        )
    )


    # Text messages

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            price_handler
        )
    )


    logger.info(
        "Bot is starting..."
    )


    app.run_polling(
        allowed_updates=Update.ALL_TYPES
    )



# ==============================
# Run
# ==============================

if __name__ == "__main__":

    main()