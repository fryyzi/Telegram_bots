import telebot
from telebot import types

class Message():
    def __init__(self, bot, message_test = "", new_persone_status = "Вкл", new_commentar_status = "Вкл", new_report_status = "Вкл"):
        self.bot = bot
        self.Message_test = message_test
        self.new_persone_status = new_persone_status
        self.new_commentar_status = new_commentar_status
        self.new_report_status = new_report_status

    def Message(self, message):
        marcup = types.InlineKeyboardMarkup()
        New_Persone = types.InlineKeyboardButton(text = "Новий учасник", callback_data = "New_Persone")
        New_commment = types.InlineKeyboardButton(text = "Новий коментар", callback_data = "New_commment")
        report = types.InlineKeyboardButton(text = "Нова жалоба", callback_data = "Report")

        marcup.row(New_Persone)
        marcup.row(New_commment)
        marcup.row(report)

        self.bot.send_message(message.chat.id, f"⚙️Повідомлення\n\nТут ви можете подивитися включені чи ваші повідомлення на якійсь функціонал:\n<b>🧑‍💼Новий учасник:</b> {self.new_persone_status}\n<b>📃Новий коментар:</b> {self.new_commentar_status}\n<b>⚠️Жалоба:</b> {self.new_report_status}", parse_mode="HTML", reply_markup=marcup)
        
        
    def Update_Persone(self, message):
        new_text = f"⚙️Повідомлення\n\nТут ви можете подивитися включені чи ваші повідомлення на якійсь функціонал:\n<b>🧑‍💼Новий учасник:</b> {self.new_persone_status}\n<b>📃Новий коментар:</b> {self.new_commentar_status}\n<b>⚠️Жалоба:</b> {self.new_report_status}"
        updated_markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Новий учасник (Викл.)", callback_data="new_Perosione_callback")).add(types.InlineKeyboardButton("Назад", callback_data = "Exit_New_Persone"))

        self.bot.send_message(message.chat.id, new_text, parse_mode="HTML", reply_markup=updated_markup)

        self.bot.edit_message_reply_markup(message.chat.id, message.message_id)


    def Unpdate_Commnets(self, message):
        new_text = f"⚙️Повідомлення\n\nТут ви можете подивитися включені чи ваші повідомлення на якійсь функціонал:\n<b>🧑‍💼Новий учасник:</b> {self.new_persone_status}\n<b>📃Новий коментар:</b> {self.new_commentar_status}\n<b>⚠️Жалоба:</b> {self.new_report_status}"

        updated_marcuk = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Новий коментар (Викл.)", callback_data = "New_commment_callbala")).add(types.InlineKeyboardButton("Назад", callback_data = "Exit_New_Persone"))
    
        self.bot.send_message(message.chat.id, new_text, parse_mode="HTML", reply_markup = updated_marcuk)
        
        self.bot.edit_message_reply_markup(message.chat.id, message.message_id)




    def Update_Report(self, message):
        new_text = f"⚙️Повідомлення\n\nТут ви можете подивитися включені чи ваші повідомлення на якійсь функціонал:\n<b>🧑‍💼Новий учасник:</b> {self.new_persone_status}\n<b>📃Новий коментар:</b> {self.new_commentar_status}\n<b>⚠️Жалоба:</b> {self.new_report_status}"

        updated_markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Новий репорт (Викл.)", callback_data = "New_Report_callbata")).add(types.InlineKeyboardButton("Назад", callback_data = "Exit_New_Persone"))

        self.bot.send_message(message.chat.id, new_text, parse_mode="HTML", reply_markup = updated_markup)
        
        self.bot.edit_message_reply_markup(message.chat.id, message.message_id)

