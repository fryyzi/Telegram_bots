import telebot
from telebot import types
import pymongo

from cogs.Run.run import Run

run = Run()

connect = pymongo.MongoClient("mongodb://localhost:27017")
db = connect["Telegram_bots"]
document = db["Tisket_Bots"]

class Start():
    def __init__(self, bot):
        self.bot = bot

    def ST(self, message):
        cursore = document.find()

        marcup = types.InlineKeyboardMarkup()
        btn_my_Tichets = types.InlineKeyboardButton(text = "🎟️Мої білети", callback_data = "btn_my_Tichets")
        btn_buy_Tickets = types.InlineKeyboardButton(text = "🎫Купити білети", callback_data = "btn_buy_Tickets")
        btn_get_Tickets = types.InlineKeyboardButton(text = "🛡️Получити білет", callback_data = "btn_get_Tickets")
        marcup.row(btn_my_Tichets, btn_buy_Tickets)
        marcup.row(btn_get_Tickets)

        for res in cursore:
            text_Condition = res.get("text_Condition")
            self.bot.send_message(message.chat.id, f"✨<b>Умови розиграшу:</b>\n {text_Condition}\nЩоб получити білети або набрать більше білетіввикористовуйте кнопки ниже👇", reply_markup = marcup, parse_mode = "HTML")
