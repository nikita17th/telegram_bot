from telebot import types
from resources.messages import yes_msg, no_msg

button_yes = types.KeyboardButton(yes_msg)
button_no = types.KeyboardButton(no_msg)
welcome_kb = types.ReplyKeyboardMarkup(resize_keyboard=True).row(yes_msg, no_msg)