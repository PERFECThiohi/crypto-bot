from cachetools import TTLCache
from config import CACHE_TIME


# ==============================
# Price Cache
# ==============================

# ذخیره قیمت ارزها
price_cache = TTLCache(
    maxsize=500,
    ttl=CACHE_TIME
)


# ==============================
# Toman Cache
# ==============================

# ذخیره قیمت تتر به تومان
usdt_cache = TTLCache(
    maxsize=1,
    ttl=CACHE_TIME
)


# ==============================
# Cache Functions
# ==============================

def get_price(symbol: str):
    """
    گرفتن قیمت ارز از کش
    """
    return price_cache.get(symbol)


def set_price(symbol: str, value: float):
    """
    ذخیره قیمت ارز در کش
    """
    price_cache[symbol] = value



def get_usdt_price():
    """
    گرفتن قیمت تتر از کش
    """
    return usdt_cache.get("usdt")


def set_usdt_price(value: float):
    """
    ذخیره قیمت تتر در کش
    """
    usdt_cache["usdt"] = value