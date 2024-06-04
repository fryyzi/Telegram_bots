import telebot
from telebot import types


i = 1

class Add_balanse:
    def __init__(self, bot):
        self.bot = bot

    
    def handle_balanse_add_balanse(self, message):
        self.bot.register_next_step_handler(message, self.add_balanse_call)

    def add_balanse_call(self, message):
        marcup_add_balanse = types.InlineKeyboardMarkup()
        add_balanse_exit_btn = types.InlineKeyboardButton(text = "⬅️Назад", callback_data = "add_balanse_exit_btn")
        marcup_add_balanse.row(add_balanse_exit_btn)
        self.bot.send_message(message.chat.id, f"<b>➕Шаг {i}/2</b>\nВведите сумму в рублях, на которую хотите пополнить баланс(Используйте только цифры)", parse_mode="HTML", reply_markup=marcup_add_balanse )
        self.bot.register_next_step_handler(message, self.add_balanse_text)

    def add_balanse_text(self, message):
        try:
            marcup = types.InlineKeyboardMarkup()
            exit_add_balanse = types.InlineKeyboardButton(text = "⬅️Назад", callback_data = "exit_add_balanse")
            pay_pay = types.InlineKeyboardButton(text = "💰Перейти к оплате", callback_data = "pay_pay")
            marcup.row(pay_pay)
            marcup.row(exit_add_balanse)
            add_balanse = int(message.text)
            self.bot.send_message(message.chat.id, f"<b>➕Шаг {i+1}/2</> \n\n<b>Сумма {add_balanse}</b>\n\n 👇Что бы оплатить перейдите по ссылке ниже и следуйте инструкциям платьожного шлюза", reply_markup = marcup , parse_mode = "HTML",)
        except ValueError:
            self.bot.send_message(message.chat.id, "❌Сумма должна состоять только из цифр <b>Попробуйте ввести снова</b>", parse_mode = "HTML")
            self.bot.register_next_step_handler(message, self.add_balanse_text)

