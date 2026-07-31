import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()


# ==============================
# Telegram Settings
# ==============================

BOT_TOKEN = os.getenv("BOT_TOKEN")


# ==============================
# Shop Settings
# ==============================

BUY_URL = os.getenv("BUY_URL")


# ==============================
# Cache Settings
# ==============================

CACHE_TIME = int(os.getenv("CACHE_TIME", 30))


# ==============================
# Logger Settings
# ==============================

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")


# ==============================
# API Settings
# ==============================

BINANCE_API = "https://api.binance.com/api/v3"

NOBITEX_API = "https://api.nobitex.ir/market/stats"


# ==============================
# Supported Coins
# ==============================

SUPPORTED_COINS = {

    # Bitcoin
    "btc": "BTCUSDT",
    "bitcoin": "BTCUSDT",
    "بیتکوین": "BTCUSDT",
    "بیت کوین": "BTCUSDT",

    # Ethereum
    "eth": "ETHUSDT",
    "ethereum": "ETHUSDT",
    "اتریوم": "ETHUSDT",
    "اتر": "ETHUSDT",

    # Tether
    "usdt": "USDTUSDT",
    "tether": "USDTUSDT",
    "تتر": "USDTUSDT",

    # Tron
    "trx": "TRXUSDT",
    "tron": "TRXUSDT",
    "tron coin": "TRXUSDT",
    "ترون": "TRXUSDT",

    # Binance
    "bnb": "BNBUSDT",
    "binance": "BNBUSDT",
    "بایننس": "BNBUSDT",

    # Solana
    "sol": "SOLUSDT",
    "solana": "SOLUSDT",
    "سولانا": "SOLUSDT",

    # Ripple
    "xrp": "XRPUSDT",
    "ripple": "XRPUSDT",
    "ریپل": "XRPUSDT",

    # Cardano
    "ada": "ADAUSDT",
    "cardano": "ADAUSDT",
    "کاردانو": "ADAUSDT",

    # Dogecoin
    "doge": "DOGEUSDT",
    "dogecoin": "DOGEUSDT",
    "دوج": "DOGEUSDT",
    "دوج کوین": "DOGEUSDT",

    # Shiba
    "shib": "SHIBUSDT",
    "shiba": "SHIBUSDT",
    "شیبا": "SHIBUSDT",

    # Ton
    "ton": "TONUSDT",
    "toncoin": "TONUSDT",
    "تون": "TONUSDT",
    "تون کوین": "TONUSDT",

    # Avalanche
    "avax": "AVAXUSDT",
    "avalanche": "AVAXUSDT",
    "آوالانچ": "AVAXUSDT",

    # Polygon
    "matic": "MATICUSDT",
    "polygon": "MATICUSDT",
    "پالیگان": "MATICUSDT",

    # Polkadot
    "dot": "DOTUSDT",
    "polkadot": "DOTUSDT",
    "پولکادات": "DOTUSDT",

    # Chainlink
    "link": "LINKUSDT",
    "chainlink": "LINKUSDT",
    "چین لینک": "LINKUSDT",

    # Litecoin
    "ltc": "LTCUSDT",
    "litecoin": "LTCUSDT",
    "لایت کوین": "LTCUSDT",

    # Meme
    "pepe": "PEPEUSDT",
    "پپه": "PEPEUSDT",

    "floki": "FLOKIUSDT",
    "فلوکی": "FLOKIUSDT",

    # AI
    "fet": "FETUSDT",
    "fetch": "FETUSDT",
    "فتچ": "FETUSDT",

    # Others
    "uni": "UNIUSDT",
    "uniswap": "UNIUSDT",
    "یونی": "UNIUSDT",

    "aave": "AAVEUSDT",
    "آوه": "AAVEUSDT",

    "atom": "ATOMUSDT",
    "cosmos": "ATOMUSDT",
    "کازماس": "ATOMUSDT",
}


# ==============================
# Validation
# ==============================

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is missing in .env")

if not BUY_URL:
    raise ValueError("BUY_URL is missing in .env")