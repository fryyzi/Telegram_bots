from telebot import types
from datetime import datetime

class Run():
    def __init__(self, bot = "", Text_Conditions = ""):
        self.bot = bot
        self.Text_Conditions = Text_Conditions

    def Runs(self, message):
        msg = self.bot.send_message(message.chat.id, "⏲️Вкажіть дату закінчення розиграша в формі <b>дд.мм.рррр</b>", parse_mode="HTML")
        self.bot.register_next_step_handler(msg, self.process_date)

    def Error_date(self, message):
        msg = self.bot.send_message(message.chat.id, "Будь ласка, введіть дату у форматі <b>дд.мм.рррр</b>", parse_mode="HTML")
        self.bot.register_next_step_handler(msg, self.process_date)


    def Conditions(self, message):
        self.text =  self.bot.send_message(message.chat.id, "✨Відправте текст з умовами розиграшу: ")
        self.bot.register_next_step_handler(self.text, self.End)
    
    def End(self, message):

        marcup = types.InlineKeyboardMarkup()
        btn_yes = types.InlineKeyboardButton(text = "✅Так", callback_data="YES")
        bnt_no = types.InlineKeyboardButton(text = "❌Ні", callback_data="NO")
        marcup.add(btn_yes, bnt_no)

        self.Text_Conditions = message.text
        self.bot.send_message(message.chat.id, f"Ви впевнені що хочете залишити цей текст?: {self.Text_Conditions}", reply_markup = marcup)

    def process_date(self, message):
        try:
            date_str = message.text
            date_obj = datetime.strptime(date_str, '%d.%m.%Y')

            self.Conditions(message)
        except ValueError:
            self.Error_date(message)

