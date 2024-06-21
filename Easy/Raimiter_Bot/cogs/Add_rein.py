import telebot
from telebot import types
import pymongo
import datetime
import random

from cogs.Review import Review

connect = pymongo.MongoClient("mongodb://localhost:27017/")
db = connect["Telegram_bots"]
document = db["reminder_bot"]
catalog = document["Reminder_db"]


class Add_rein:
    def __init__(self, bot):
        self.bot = bot

    def add(self, message):
        markup = types.InlineKeyboardMarkup()
        btn_next = types.InlineKeyboardButton(text="Далі", callback_data="btn_next")
        markup.row(btn_next)
        self.bot.send_message(message.chat.id, 
            "📋 Напишіть свій список дій або що там потрібно вам 😁\n\n"
            "✍️ Писати потрібно через пробіл, якщо ви відправите текст, то він автоматично занесеться в список.\n\n"
            "<b>❗ Тому відправляйте або через пробіл, або з нового рядка</b> 😉\n\n",
            parse_mode="HTML", reply_markup=markup)

    def handler(self, message):
        self.bot.send_message(message.chat.id, "🔽Чекаю твоє повідомлення🔽")
        self.bot.register_next_step_handler(message, self.add_test)

    def add_test(self, message):
        try:
            user_text = message.text
            
            self.bot.send_message(message.chat.id, f"Ваше повідомлення збережено! {user_text}")
            first_name = message.from_user.first_name
            user_name = message.from_user.username
            id_user = message.from_user.id
            now = datetime.datetime.now()
            year = now.year
            month = now.month
            day = now.day
            add_db = {

                "Name": first_name,
                "Nick_Name": user_name,
                "Id_user": id_user,
                "Message_id":  random.randint(0, 100000),
                "Text": user_text,
                "Year": year,
                "Month": month,
                "Day": day,
                "Time": now

            }
            catalog.insert_one(add_db)

        except:
            self.bot.send_message(message.chat.id, "Сталась невідома помилка повторіть спробу ще раз!")

