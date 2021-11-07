import telebot
from handlers.welcome_handler import handle_welcome
from resources.token import token

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    handle_welcome(message)


bot.polling(none_stop=True, interval=0)
