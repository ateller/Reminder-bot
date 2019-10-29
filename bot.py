import telebot
import time
import random
import os
from threading import Thread

from telebot import apihelper
from config import token, prox_ip, id, text_variants, period, add_punish_time

def remind():
	try:
		bot.send_message(id, random.choice(text_variants), parse_mode = 'HTML')
		return False
	except Exception:
		return True

def remind_in_cycle():
	while True:
		if not add_in_process:
			i = 0
			while remind() and (i < 100):
				time.sleep(1)
				i += 1
			time.sleep(period)
		elif time.time() - add_time > add_punish_time:
			bot.send_message(id, 'Ха, нажимаешь команду и ничего не делаешь, чтобы не приходили напоминания? Умный ход, но я все вижу! Быстра пиши, что там надо писать, а то это будет отправляться каждые 5 минут')
			time.sleep(300)
		else:
			time.sleep(100)
		
def listen():
	while True:
		try:
			bot.polling(none_stop = True, interval = 0, timeout = 20)
		except Exception:
			pass

def add(message):
	global add_in_process
	if message.from_user.id == id:
		try:
			if (not message.text) or (message.text[0] == '/'):
				msg = bot.reply_to(message, 'Текста нет, пиши еще раз, только текст, бот пока не умеет ничего кроме')
				bot.register_next_step_handler(msg, add)
			else:
				text_variants.append(message.text)
				bot.reply_to(message, 'Вроде добавил')
				add_in_process = False
		except Exception as a:
			print(str(a))
			bot.send_message(id, 'Произошло что-то неправильное и я(бот) упал')
			os._exit(0)

apihelper.proxy = {'https':prox_ip} #Спасибо ркн
bot = telebot.TeleBot(token) 
print(bot.get_me()) #Проверка, что мы справились с ркн
add_in_process = False
add_time = 0

@bot.message_handler(commands=['add'])
def reply_to_comand_add(message):
	global add_in_process
	global add_time
	if (message.from_user.id == id) and (add_in_process == False):
		try:
			msg = bot.reply_to(message, 'Напиши следующим сообщением, что хочешь добавить. Выбирай мудро, что хочешь написать, удалять без перезапуска бота нельзя пока. Пока не закончишь добавление кстати, напоминаний не будет')
			bot.register_next_step_handler(msg, add)
			add_in_process = True
			add_time = time.time()
		except Exception as a:
			print(str(a))
			bot.send_message(id, 'Произошло что-то неправильное и я(бот) упал')
			os._exit(0)

@bot.message_handler(commands=['show'])
def reply_to_comand_add(message):
	if message.from_user.id == id:
		try:
			text = ''
			for variant in text_variants:
				text += variant + '\n'
			bot.reply_to(message, text)
		except Exception as a:
			print(str(a))
			bot.send_message(id, 'Произошло что-то неправильное и я(бот) упал')
			os._exit(0)

thread1 = Thread(target = listen, daemon = True)
thread2 = Thread(target = remind_in_cycle, daemon = True)

thread1.start()
thread2.start()