import requests
import json
from config import keys


class ConversionException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise ConversionException(f"Не удалось перевести одинаковые валюты {base}. ")

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConversionException(f"Не удалось обработать валюту {quote}. ")

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConversionException(f"Не удалось обработать валюту {base}. ")

        try:
            amount = float(amount)
        except:
            raise ConversionException(f"Не удалось обработать количество {amount}. ")

        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}")
        exchange_rate = float(json.loads(r.content)[base_ticker])
        total_base = amount * exchange_rate
        text = f'{quote} {amount} => {base} {total_base}'
        return text
