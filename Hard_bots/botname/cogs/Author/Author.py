import telebot
from telebot import types

from cogs.Approve.Approve import Approve

approve = Approve()

class Author():

    global Author_Channel
    def __init__(self, bot):
        self.bot = bot

    def Author(self, message):
        Author_Channel = 1
        if Author_Channel == 1:
            Channel = types.InlineKeyboardMarkup()
            Channel_name = types.InlineKeyboardButton(text = approve.channel, callback_data = approve.channel)
            Channel.row(Channel_name)
            self.bot.send_message(message.chat.id, "👑Тут ви - автор. Ви можете вибрати группу і настроїти все так як пожелаєте\n💰<b>Так же ви можете управляти своїми платними ресурсами:</b>\n\n➖Встановити ціну\n➖Сформувати Whilelist - представляя ізбранимкористувачам право знаходитись в группі без оплати\n\n❗Увага\nЯкщо ви не желаєте втрачувати стару группу то для вас є функція перевірка учасників\n\nЗ цією функцією ви можете подключити любу текущу группу загрузивши бота список текущих учасників\n\nБот проверяє список учасників і починає модерацію в стандартному порядку", reply_markup = Channel, parse_mode="HTML")
        