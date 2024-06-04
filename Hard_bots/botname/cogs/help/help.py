from telebot import types
import pymongo

connect = pymongo.MongoClient("mongodb://localhost:27017")
db = connect["botname"]
Helps = db["Help_text"]

class Help:
    def __init__(self, bot):
        self.bot = bot

    def handle_help(self, message):
        self.bot.register_next_step_handler(message, self.Complited)

    def Help_menu(self, message):
        Sapport_marlup = types.InlineKeyboardMarkup()
        Sapport_button = types.InlineKeyboardButton(text="⏲️Нужна помочь", callback_data="Sapport_button")
        Sapport_marlup.row(Sapport_button)

        self.bot.send_message(message.chat.id, text="❗Перед тим як писати питання, перевірте чи не було такого питання у когось іншого.\nЯкщо ви ніде не знайшли відповідь, натисніть кнопку нижче👇", reply_markup=Sapport_marlup)

    def Complited(self, message):
        Exit_Chat = types.InlineKeyboardMarkup()
        Exit_Chat_Button = types.InlineKeyboardButton(text="❌Завершити розмову", callback_data="Exit_Chat_Button")
        Exit_Chat.row(Exit_Chat_Button)

        self.bot.send_message(message.chat.id,
                              text=f"Перед тим як написати свою проблему, будь ласка, прочитайте нижче:\n\n"
                                   f"1️⃣ Будь ласка, сформулюйте своє повідомлення в одне повідомлення і напишіть тільки суть повідомлення.\n\n"
                                   f"2️⃣ Не відправляйте нічого крім тексту.\n\n"
                                   f"3️⃣ Будьте дружелюбні",
                              reply_markup=Exit_Chat)

        self.bot.register_next_step_handler(message, self.test)

    def test(self, message):

        add_Help_Text = {
            "Name": message.chat.first_name,
            "Text": message.text,
            "User_Name": message.chat.username
        }
        Helps.insert_one(add_Help_Text)


    def Help_Persone():
        print("test")

        
