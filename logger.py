import logging

from config import LOG_LEVEL


# ==============================
# Logger Configuration
# ==============================

logging.basicConfig(
    level=LOG_LEVEL,
    format=(
        "%(asctime)s | "
        "%(levelname)s | "
        "%(message)s"
    ),
    handlers=[
        logging.FileHandler(
            "bot.log",
            encoding="utf-8"
        ),
        logging.StreamHandler()
    ]
)


# ==============================
# Main Logger
# ==============================

logger = logging.getLogger("CryptoBot")