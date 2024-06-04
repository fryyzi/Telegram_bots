import telebot
from telebot import types
import pymongo

connect = pymongo.MongoClient("mongodb://localhost:27017")
db = connect["botname"]
Withdraw_collection = db["Withdraw"]
User_collection = db["User"]

class CommandHandler:
    def __init__(self, bot):
        self.bot = bot


    def handle_start(self, message):
        markup = types.InlineKeyboardMarkup()

        Balance = types.InlineKeyboardButton(text="Баланс📍", callback_data="Balance")
        markup.row(Balance)

        Support = types.InlineKeyboardButton("🍰Поддержка", callback_data="Support")
        Comments = types.InlineKeyboardButton("✏️Комментарии", callback_data="Comments")
        markup.row(Support, Comments)

        Subscriptions = types.InlineKeyboardButton("🔥Подписки", callback_data="Subscriptions")
        markup.row(Subscriptions)

        collection = types.InlineKeyboardButton("💰Идёт сбор", callback_data="collection")
        markup.row(collection)

        help_button = types.InlineKeyboardButton("Зачем бот❓", callback_data="help")
        markup.row(help_button)
    
        self.bot.send_message(message.chat.id, "Добро пожаловать на botname\n\n📌Бот позволяєт монетизировать продажу ваших уникальных материалов в группах.Также монетизирует комментарии пользователей🔥", reply_markup=markup)
        add_user = {
            "Name_User": message.chat.first_name,
            "User_name": message.chat.username,
            "Id_User": message.from_user.id,
            "Permission": "User",
            "balanse": 0
        }
        User_collection.insert_one(add_user)

