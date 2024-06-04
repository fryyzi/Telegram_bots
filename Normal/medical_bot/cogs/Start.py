from telebot import types

class Start():
    def __init__(self, bot):
        self.bot = bot

    def start(self, message):
        marcup = types.InlineKeyboardMarkup()
        about_us = types.InlineKeyboardButton(text = "Про нас", callback_data = "about_us")
        serve = types.InlineKeyboardButton(text = "Послуги", callback_data = "serve")
        our_doctors = types.InlineKeyboardButton(text = "Наші лікарі", callback_data = "our_doctors")
        Record = types.InlineKeyboardButton(text = "Записатися до лікаря", callback_data = "Record")
        marcup.add(about_us, serve, our_doctors, Record)
        self.bot.send_message(message, "Вітаємо Вас у чат боті медичного центра\n'BestMedicine'", reply_markup = marcup)