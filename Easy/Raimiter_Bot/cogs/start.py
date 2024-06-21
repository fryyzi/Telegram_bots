import telebot
from telebot import types

import pymongo

connect = pymongo.MongoClient("mongodb://localhost:27017/")
db = connect["Telegram_bots"]
document = db["reminder_bot"]
catalog = document["Reminder_db"]


class Start():
    def __init__(self, bot = None):
        self.bot = bot

    def start(self, message):

        marcup = types.InlineKeyboardMarkup()
        add_rein = types.InlineKeyboardButton("Додати нагадування", callback_data = "add_rein")
        review = types.InlineKeyboardButton("Переглянути нагадування", callback_data = "review")
        delete_message = types.InlineKeyboardButton("Видалити нагадування", callback_data = "delete_message")
        marcup.row(add_rein, review)
        marcup.row(delete_message)
        msg = "👋 Ласкаво просимо до бота для нагадувань!\n\n📅 Тут ви зможете вписати всі ваші плани і в будь-який момент їх переглянути.\n\n<b>🌐Головне, щоб був інтернет.😊</b>"
        

        
        self.bot.send_message(message.chat.id, msg, reply_markup = marcup, parse_mode = "HTML")