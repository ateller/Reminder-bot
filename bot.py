import telebot
import time

from telebot import apihelper
from config import token, id, text, period

def remind():
    try:
        bot.send_message(id, text, parse_mode = 'HTML')
        return False
    except Exception:
        return True

bot = telebot.TeleBot(token) 
print(bot.get_me())

while True:
    i = 0
    while remind() and (i < 100):
        time.sleep(1)
        i += 1
    time.sleep(period)
