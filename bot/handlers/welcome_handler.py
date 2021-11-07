import sys
import telebot
sys.path.insert(0, '../resources')
from resources.token import token
from resources.messages import welcome_msg
from keyboars.welcome_kb import welcome_kb

bot1 = telebot.TeleBot(token)


def handle_welcome(message):
    bot1.send_message(message.from_user.id, welcome_msg, reply_markup=welcome_kb)
