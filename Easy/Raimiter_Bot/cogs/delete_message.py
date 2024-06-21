import telebot
from telebot import types
import pymongo

connect = pymongo.MongoClient("mongodb://localhost:27017/")
db = connect["Telegram_bots"]
document = db["reminder_bot"]
catalog = document["Reminder_db"]


class Delete_Message():
    def __init__(self, bot, id_main_user = None ,delete = 0, id_message = 0):
        self.bot = bot

        self.delete = delete
        self.id_main_user = id_main_user

        self.id_message = id_message


    def delete_msg(self, message_chat_id , id_persone = 0):
        marcup = types.InlineKeyboardMarkup()

        query = catalog.find({"Text": {"$exists": True}, "Message_id": {"$exists": True}, "Id_user": {"$exists": True}})
        for message in query:
            Text = message.get("Text")
            self.id_message = message.get("Message_id")
            id_user = message.get("Id_user")

            if id_persone == id_user:
                delete_btn = types.InlineKeyboardButton(text = self.id_message, callback_data = f"id_message_{self.id_message}")
                marcup.row(delete_btn)
                self.bot.send_message(message_chat_id.chat.id, f"<b>Нагадування:</b>\n\n{Text}\n\n <b>Id вашого нагадування:</b> {self.id_message}", parse_mode = "HTML")
        self.bot.send_message(message_chat_id.chat.id, "Виберіть номер свого повідомлення", reply_markup = marcup)




        # self.id_main_user = id_us
        # query_id = catalog.find({"Message_id": {"$exists": True}})
        # query_message = catalog.find()
        # user_id = catalog.find({"Id_user": {"$exists": True}})
        # for message_id in query_id:
        #     id_message = message_id.get("Message_id")
        # for message_text in query_message:
        #     Text = message_text.get("Message_id")
        # for id_user in user_id:
        #     id_users = id_user.get("Id_user")
        # if id_message == Text:
        #     print("test")
        #     print(self.id_main_user)
        #     # print(id_users)
        #     if id_users == self.id_main_user:
        #         print("1")
        #         print(id_users)
        #         print(self.id_main_user)
        #         print("test")
        #         # catalog.delete_one({"Message_id": id_message})
        # else:
        #     print("test")
        

