import telebot
from telebot import types

from cogs.Approve.Approve import Approve

approve = Approve()

class Channel():
    def __init__(self, bot = None, channel_name = "", price = 0):
        self.bot = bot
        self.channel_name = channel_name
        self.price = price

    def Channel_main(self, message):
        markup = types.InlineKeyboardMarkup()
        Message = types.InlineKeyboardButton(text = "⚙️Повідомлення", callback_data = "Message")
        Stop = types.InlineKeyboardButton(text = "❗Стоп", callback_data = "Stop")
        Strict_Controle = types.InlineKeyboardButton(text = "🔐Строгий контроль", callback_data = "Strict_Controle")
        Edit_money = types.InlineKeyboardButton(text = "✏️Змінити ціну", callback_data = "Edit_money")
        Edit_WhileList = types.InlineKeyboardButton(text = "📃Редиактіровать WhileList", callback_data = "Edit_WhileList")
        Invite_Persone = types.InlineKeyboardButton(text = "➕Пригласити подпіщика", callback_data = "Invite_Persone")
        Actual_Sub = types.InlineKeyboardButton(text = "⚕️Актуальні підписники", callback_data = "Actual_Sub")
        Delete_channnel = types.InlineKeyboardButton(text = "➖Видалити", callback_data = "Delete_channnel")

        markup.row(Message)
        markup.row(Stop)
        markup.row(Strict_Controle)
        markup.row(Edit_money)
        markup.row(Edit_WhileList)
        markup.row(Invite_Persone)
        markup.row(Actual_Sub)
        markup.row(Delete_channnel)
        self.bot.send_message(message.chat.id, f"<b>Назва</b>: {approve.channel}\n<b>Статутс</b>: Работає\n<b>\n<b>Ціна: {self.price}\n</b>Подпіщиков на каналі</b>: 3\n<b>Строгій контроль </b>: Включений\n<b>WheliLIst</b>: 3\n<b>Платять</b>: 997", reply_markup=markup, parse_mode="HTML")


    def handle_Price(self, message):
        self.bot.register_next_step_handler(message, self.Price)

    def Price(self, message):
        self.bot.send_message(message.chat.id, f"<b>Мінімальна сумма:</b> 500 грн\nВведіть цену за 1 місяц підписки на ваш чат(Використовуйте тільки цифри)\n\nЯкщо ви хочете щоб підписка була безкоштовна <b>вкажіть</b> - 0", parse_mode = "HTML")
        self.bot.register_next_step_handler(message, self.Price_Update) 

    def Price_Update(self, message):
        try:
            Price = int(message.text)
            if Price < 500:
                self.bot.send_message(message.chat.id, "<b>❌Мінімальна сумма:</b> 500 грн\n<b>Спробуйте вести знову!:</b>", parse_mode = "HTML")
                self.bot.register_next_step_handler(message, self.Price_Update)
            else:
                self.price = Price
                self.bot.send_message(message.chat.id, "<b>✏️✔️Сумма підписки успішно виправленна</b>", parse_mode = 'HTML')
        except:
            self.bot.send_message(message.chat.id, "❌Сумма повинна бути дільки з цифр.<b>Спробуйте знову:</b>", parse_mode = "HTML")
            self.bot.register_next_step_handler(message, self.Price_Update)
