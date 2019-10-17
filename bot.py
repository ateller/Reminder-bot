import telebot
import time

from telebot import apihelper
from config import token, prox_ip, id, text, period

def remind():
    try:
        bot.send_message(id, text, parse_mode = 'HTML')
        return False
    except Exception:
        return True

apihelper.proxy = {'https':prox_ip} #Спасибо ркн
bot = telebot.TeleBot(token) 
print(bot.get_me()) #Проверка, что мы справились с ркн

while True:
    i = 0
    while remind() and (i < 100):
        time.sleep(1)
        i += 1
    time.sleep(period)
