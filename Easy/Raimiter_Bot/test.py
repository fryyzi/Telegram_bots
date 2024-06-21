# import telebot
# from cogs.bot_logic import BotLogic

# # Введіть ваш токен бота тут
# API_TOKEN = '7488404684:AAFaelKeDHmzdLiAc0q-Wl8Urk5lY2GWxjs'
# bot = telebot.TeleBot(API_TOKEN)

# bot_logic = BotLogic(bot)

# @bot.message_handler(commands=["start"])
# def start(message):
#     bot.send_message(message.chat.id, "Ласкаво просимо! Введіть текст для кнопки:")

# @bot.message_handler(func=lambda message: True)
# def handle_message(message):    
#     bot_logic.create_button(message)

# bot.polling(non_stop=True)

# import pymongo

# connect = pymongo.MongoClient("mongodb://localhost:27017/")
# db = connect["Telegram_bots"]
# document = db["reminder_bot"]
# catalog = document["Reminder_db"]

# cursor = catalog.find({"Year": {"$exists": True}}, {"Year": 1, "_id": 0})

# for document in cursor:
#     print(document)

# import random

# print(random.randint(0, 100000))

import pymongo

connect = pymongo.MongoClient("mongodb://localhost:27017/")
db = connect["Telegram_bots"]
document = db["reminder_bot"]
catalog = document["Reminder_db"]


documents = catalog.find()

for doc in documents:
    id_user = doc['Id_user']['$numberLong']
    print(f"Id_user: {id_user}")

    # Ви можете також вивести інші поля документа
    print(doc)
