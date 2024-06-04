import telebot
from telebot import types
import pymongo


connect = pymongo.MongoClient("mongodb://localhost:27017")
db = connect["botname"]
Withdraw_collection = db["Withdraw"]
User_collection = db["User"]


number = 1
number_balanse = 100

class Withdraw:
    def __init__(self, bot):
        self.bot = bot

    def dalanse(self, message):
        marcup = types.InlineKeyboardMarkup()
        add_balanse = types.InlineKeyboardButton(text="➕Пополнить", callback_data="add_balanse")
        withdraw = types.InlineKeyboardButton("➖Вывести", callback_data="Withdraw")
        marcup.row(add_balanse, withdraw)
        exit_button = types.InlineKeyboardButton("Назад", callback_data="exit_main_menu")
        marcup.row(exit_button)
        self.bot.send_message(message.chat.id, f"👉*Баланс* {number_balanse} руб\n\n👇Воспользуйтесь кнопками ниже, чтобы пополнить или вывести свои средства", reply_markup=marcup, parse_mode="Markdown")
