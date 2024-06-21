import telebot
from telebot import types
import pymongo


connect = pymongo.MongoClient("mongodb://localhost:27017/")
db = connect["Telegram_bots"]
document = db["reminder_bot"]
catalog = document["Reminder_db"]


class Delete():
    def __init__(self, bot, number_button = 0, year = 0):
        self.bot = bot

        self.year = year
        self.number_button = number_button

    def delete_message(self, message):
        document = catalog.find_one()
        if document:
            self.year = document.get("Year")
        user_message = catalog.find({"Id_user": {"$exists": True}})
        for res in user_message:
            id_user = res.get("Id_user")
        id = message.from_user.id    
        # print(id_user)
        # print(id)
        if self.year == 0:
            self.number_button = 0
        elif self.year >= 2023:
            self.number_button = 1

        if self.number_button == 0:
            print(self.number_button)
            marcup = types.InlineKeyboardMarkup()
            delete_message = types.InlineKeyboardButton(text = "У вас немає жодного нагадування", callback_data = "year_message_{self.year}")
            marcup.add(delete_message)
            self.number_button += 1
        elif self.number_button >= 1:
            marcup = types.InlineKeyboardMarkup()
            btn_year = types.InlineKeyboardButton(text = self.year, callback_data=f"year_message_{self.year}")
            marcup.add(btn_year)
        
        self.bot.send_message(message.chat.id, text = "Виберіть рік де знаходиться ваше нагадування", reply_markup = marcup)


