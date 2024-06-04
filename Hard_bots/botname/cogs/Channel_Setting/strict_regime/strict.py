import telebot
from telebot import types


class Strict():
    def __init__(self, bot, status = "Викл"):
        self.bot = bot
        self.status = status

    def Strict_def(self, message):
        markup = types.InlineKeyboardMarkup()
        Stop_btn = types.InlineKeyboardButton(text = "Включити", callback_data = "On_btn")
        exit_btn = types.InlineKeyboardButton(text = "Назад", callback_data = "exit_btn")
        markup.row(Stop_btn)
        markup.row(exit_btn)

        self.bot.send_message(message.chat.id, f"Ця функція стоїть виключить якщо ви хочете щоб заявка на вступ міг одобрити не тільки цей\n\nНажміть на кнопку ниже щоб змінити статус\nСтатус: {self.status}", reply_markup = markup)

    def Update_Button(self, message):
        new_text = f"Ця функція стоїть виключить якщо ви хочете щоб заявка на вступ міг одобрити не тільки цей\n\nНажміть на кнопку ниже щоб змінити статус\nСтатус: {self.status}"

        update_markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Виключити", callback_data = "On_stri")).add(types.InlineKeyboardButton("Назад", callback_data = "Str_exit"))

        self.bot.send_message(message.chat.id, new_text, parse_mode="HTML", reply_markup = update_markup)
        self.bot.edit_message_reply_markup(message.chat.id, message.message_id)