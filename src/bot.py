import os
import telebot
from config import TOKEN
from service import link_to_qr


bot = telebot.TeleBot(TOKEN,parse_mode=None)


@bot.message_handler(commands=['start','pls', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    path = link_to_qr(message.text)   # забирать ссылки и через йнкцию создавать
    bot.reply_to(message, message.text) # отвечавть на смс
    photo = open(path,'rb')
    print(message.chat.id)
    bot.send_photo(message.chat.id, photo)
    os.remove(path)

bot.polling()
