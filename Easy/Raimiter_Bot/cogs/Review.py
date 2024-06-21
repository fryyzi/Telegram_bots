import telebot
from telebot import types
import pymongo
import datetime

connect = pymongo.MongoClient("mongodb://localhost:27017/")
db = connect["Telegram_bots"]
document = db["reminder_bot"]
catalog = document["Reminder_db"]

class Review():
    def __init__(self, bot = None, year = 0, month = 0, day = 0, number_button = 1, text = "", id_user = 0, id_main = 0):
        self.bot = bot
        self.year = year
        self.month = month
        self.day = day

        self.existing_buttons = set()

        self.number_button = number_button
        self.text = text

        self.id_user = id_user
        self.id_main = id_main

        self.markup = types.InlineKeyboardMarkup()

    def review_reminded(self, message):
        document = catalog.find_one()
        now = datetime.datetime.now()
        if document:
            self.year = document.get("Year")
        if message is not None:
            if self.id_main != self.id_user:
                button_text = "У вас немає жодних нагадувань!"
                if button_text not in self.existing_buttons:
                    button = types.InlineKeyboardButton(text=button_text, callback_data=f"year_{self.year}")
                    self.markup.row(button)
                    self.existing_buttons.add(button_text)
            
            if self.year == now.year:
                if self.id_main == self.id_user:
                    button_text = f"Рік {self.year}"
                    if button_text not in self.existing_buttons:
                        button = types.InlineKeyboardButton(text=button_text, callback_data=f"year_{self.year}")
                        self.markup.row(button)
                        self.existing_buttons.add(button_text)
                pass
            if self.year != now.year:
                print("Роки не збігаються")

            




            # if self.id_main == self.id_user:
            #     button = types.InlineKeyboardButton(text=f"Рік {self.year}", callback_data=f"year_{self.year}")
            #     if self.year == now.year:
            #         print("Роки збігаютться ")
            #     else:
            #         print("Роки не збігаються")
            #         self.markup.row(button)
            if message == None:
                pass
            else:
                self.bot.send_message(message.chat.id, text="Виберіть рік", reply_markup=self.markup)
        else:
            pass


