import requests

from config import BINANCE_API

from cache import (
    get_price,
    set_price,
    get_usdt_price,
    set_usdt_price
)


# ==============================
# Binance Coin Price
# ==============================

def get_coin_price(symbol: str):

    cached = get_price(symbol)

    if cached:
        return cached

    try:

        url = f"{BINANCE_API}/ticker/price"

        response = requests.get(
            url,
            params={"symbol": symbol.upper()},
            timeout=10
        )

        data = response.json()

        price = float(data["price"])

        set_price(symbol, price)

        return price

    except Exception as e:

        print("BINANCE ERROR:", e)

        return None



# ==============================
# USDT Toman Price
# ==============================

def get_usdt_toman():

    cached = get_usdt_price()

    if cached:
        return cached


    try:

        url = "https://api.tetherland.com/currencies"

        response = requests.get(
            url,
            timeout=10
        )

        data = response.json()


        usdt_price = float(
            data["data"]["currencies"]["USDT"]["price"]
        )


        set_usdt_price(
            usdt_price
        )


        return usdt_price


    except Exception as e:

        print("USDT ERROR:", e)

        return None



# ==============================
# Calculate
# ==============================

def calculate_toman(symbol, amount):

    coin_price = get_coin_price(symbol)

    if coin_price is None:
        return None


    usdt_price = get_usdt_toman()

    if usdt_price is None:
        return None


    return round(
        coin_price *
        usdt_price *
        amount
    )