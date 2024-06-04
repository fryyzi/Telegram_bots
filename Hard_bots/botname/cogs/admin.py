from telebot import types
import pymongo

connect = pymongo.MongoClient("mongodb://localhost:27017")
db = connect["botname"]
User_collection = db["User"]

class Admin():
    def __init__(self, bot):
        self.bot = bot

    def admin(self, message):
        admin_Markup = types.InlineKeyboardMarkup()
        Withdeaw_admin = types.InlineKeyboardButton(text = "Выводы", callback_data = "Withdeaw_admin")
        add_admin = types.InlineKeyboardButton(text = "Добавить админа", callback_data = "Add_admin")
        add_balanse = types.InlineKeyboardButton(text = "Добавити баланс", callback_data = "add_balanse_admin")
        Help_Menu = types.InlineKeyboardButton(text = "Допомога", callback_data="Admin_Help_Menu")
        admin_Markup.row(Withdeaw_admin)
        admin_Markup.row(add_admin, add_balanse)
        admin_Markup.row(Help_Menu)
        self.bot.send_message(message.chat.id, "Выберете пункт:", reply_markup=admin_Markup)


    def handle_balanse_request(self, message):
        self.bot.register_next_step_handler(message.chat.id, self.process_balanse_amount)

    def process_balanse_amount(self, message):
        marcup = types.InlineKeyboardMarkup()
        exit_balanse = types.InlineKeyboardButton(text="⬅️Назад",  callback_data="exit_balanse_card")
        marcup.add(exit_balanse)
        self.bot.send_message(message.chat.id, f"Введіть баланс", reply_markup=marcup, parse_mode="HTML")
        self.bot.register_next_step_handler(message, self.balanse_text)

    
    def balanse_text(self, message):
        add_balanse = int(message.text)
        try:
            cursore = User_collection.find()
            for i in cursore:
                User_balanse = i.get("balanse")
            self.bot.send_message(message.chat.id, "Готово")
            User_collection.update_many({"balanse": User_balanse}, {'$set': {"balanse": add_balanse}})
        except ValueError:
            self.bot.send_message(message.chat.id, "❌Неверный формат ввода карты\n<b>Пример</b> 5454 5454 5454 5454\n<b>Попробуйте ввести снова:</b>", parse_mode="HTML")
            self.handle_balanse_request(message,self.process_balanse_amount)

        