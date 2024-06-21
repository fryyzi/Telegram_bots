import telebot
import pymongo
from telebot import types

from cogs.start import Start
from cogs.Add_rein import Add_rein
from cogs.Review import Review
from cogs.delete_rain import Delete
from cogs.delete_message import Delete_Message

connect = pymongo.MongoClient("mongodb://localhost:27017/")
db = connect["Telegram_bots"]
document = db["reminder_bot"]
catalog = document["Reminder_db"]

bot = telebot.TeleBot("7488404684:AAFaelKeDHmzdLiAc0q-Wl8Urk5lY2GWxjs")


start_bot = Start(bot)
add_rein = Add_rein(bot)
review = Review(bot)
delete = Delete(bot)
delete_message = Delete_Message(bot)

@bot.message_handler(commands=["start"])
def start(message):
    global userse
    userse = message.from_user.id
    start_bot.start(message)
    # print(users)
    # review.review_reminded(message=None, id = userse)
    # delete_message.delete_msg(id_us = userse)

    # bot.send_message(message.chat.id, message)

@bot.callback_query_handler(func=lambda call: True)
def call_data(call):
    cursor = catalog.find({"Year": {"$exists": True}})
    for document in cursor:
        if call.data == f"year_{document.get('Year')}":
            try:
                user_id = catalog.find({"Id_user": {"$exists": True}, "Text": {"$exists": True}})
                prev_text = []
                i = True
                while i:
                    for res in user_id:
                        id = res.get("Id_user")
                        text = res.get("Text")
                        if text in prev_text:
                            pass
                        else:
                            if userse == id:
                                bot.send_message(call.message.chat.id, text=text)
                                prev_text.append(text)
                            else:
                                bot.send_message(call.message.chat.id, "У вас немає жодних повідомлень за цей рік!")
            except:
                bot.send_message(call.message.chat.id, "У вас немає жодних повідомлень за цей рік!")

    if call.data == "btn_delete":
        delete_message.delete_msg(call.message)

    if call.data == "add_rein":
        add_rein.add(call.message)
    elif call.data == "btn_next":
        add_rein.handler(call.message)
    elif call.data == "review":
        user_id = catalog.find({"Id_user": {"$exists": True}})
        for id in user_id:
             id_usere= id.get("Id_user")
        review.review_reminded(call.message)
    elif call.data == "delete_message":
        delete_message.delete_msg(call.message, id_persone = userse)

    cursor_year = catalog.find({"Year": {"$exists": True}})
    for years in cursor_year:
        if call.data == f"year_message_{years.get("Year")}":
            print("test")
            user_message = catalog.find({"Id_user": {"$exists": True}, "Text": {"$exists": True}})
            massive_text = []
            y = True
            while y:
                for res in user_message:
                    id_user = res.get("Id_user")
                    user_message_text = res.get("Text")
                    if user_message_text in massive_text:
                        pass
                    else:
                        if id_user == userse:
                            bot.send_message(call.message.chat.id, text=user_message_text)
                            massive_text.append(user_message_text)

    query_id_message = catalog.find({"Message_id": {"$exists": True}})
    for id_Message in query_id_message:
        if call.data == f"id_message_{id_Message.get("Message_id")}":
            catalog.delete_one({"Message_id": id_Message.get('Message_id')})
            bot.send_message(call.message.chat.id, "Ваше нагадування було успішно видаленно")
            

@bot.message_handler(commands=["id"])
def test(message):
    bot.send_message(message.chat.id, message)
    user_message = catalog.find({"Id_user": {"$exists": True}, "Text": {"$exists": True}})
    for res in user_message:
        id_user = res.get("Id_user")
        try:
            bot.send_message(message.chat.id, id_user)
        except:
            bot.send_message(message.chat.id, "Не вдалося вивести id")


bot.polling(non_stop=True)