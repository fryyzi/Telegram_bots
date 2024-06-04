import telebot
from telebot import types


class MY_Ticket():
    def __init__(self, bot):
        self.bot = bot

    def my_ticket(self, message):
        markup = types.InlineKeyboardMarkup()
        Exit_my_ticket = types.InlineKeyboardButton(text = "Назад", callback_data = "Exit_my_ticket")
        markup.add(Exit_my_ticket)

        self.bot.send_message(message.chat.id, "<b>Мої білети\n ")
        
        