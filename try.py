'''
pip3 install pyTelegramBotAPI

import telebot
bot = telebot.TeleBot('TOKEN')

TOKEN = "1407844531:AAHqV7-_DYhiwXxzcIxaeLg0Dk10hqPX-RQ"

bot = telebot.TeleBot(TOKEN)

bot.polling(none_stop=True)

import telebot
bot = telebot.TeleBot('TOKEN')

TOKEN = "1407844531:AAHqV7-_DYhiwXxzcIxaeLg0Dk10hqPX-RQ"

bot = telebot.TeleBot(TOKEN)




@bot.message_handler(filters)
def function_name(message):
    bot.reply_to(message, "This is a message handler")

EUR RUB 100


@bot.message_handler(content_types=["text", ])
def convert(message: telebot.types.Message):
    try:
        quote, base, amount = message.text.split(" ")
        r = requests.get("https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}".format(quote, base))
        rate_json = r.json()
        rate = float(rate_json[base])
        text = str(float(amount)*rate)
        bot.send_message(message.chat.id, text)
    except:
        bot.send_message(message.chat.id, "Error")

import telebot
import requests
import json
from config import keys, TOKEN
from while import Convertionexception, Cryptoconverter


bot = telebot.TeleBot(TOKEN)


class Convertionexception(Exception):
    pass


@bot.message_handler(commands=["start", "help"])
def help(message: telebot.types.Message):
    text = "Чтобы начать работу, введите команду боту в следующем формате:\имя валюты" \
"в какую валюту перевести" \
"количество переводимой валюты", "увидеть список всех доступных валют: /values"
    bot.reply_to(message, text)


@bot.message_handler(commands=["values"])
def values(message: telebot.types.Message):
    text = "Доступные валюты"
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=["text", ])
def convert(message: telebot.types.Message):
    values = message.text.split(" ")

    if len(values) > 3:
        raise Convertionexception("Слишком много параметров. ")

    quote, base, amount = values

    if quote == base:
        raise Convertionexception(f"Не удалось перевести одинаковые валюты {base}. ")

    try:
        quote_ticker = keys[quote]
    except KeyError:
        raise Convertionexception(f"Не удалось обработать валюту {quote}. ")

    try:
        base_ticker = keys[base]
    except KeyError:
        raise Convertionexception(f"Не удалось обработать валюту {base}. ")

    try:
        amount = float(amount)
    except KeyError:
        raise Convertionexception(f"Не удалось обработать количество {amount}. ")

    quote_ticker, base_ticker = keys[quote], keys[base]
    r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym=(quote_ticker)&tsyms=(base_ticker)")
    total_base = json.loads(r.content)[keys[base]]
    text = f'Цена (amount) (quote) * (base) - (total_base)'
    bot.send_message(message.chat.id, text)




bot.polling()

'''

