import telebot
import pymongo
from cogs.Run.run import Run
from cogs.Start.start import Start
from cogs.Ticket.Buy_Ticket import Buy_Ticket

bot = telebot.TeleBot("6740909089:AAFsHKxhG0YXTSBXG1RJStcp8SdIxyavhUw")

connect = pymongo.MongoClient("mongodb://localhost:27017")
db = connect["Telegram_bots"]
document = db["Tisket_Bots"]

run_text = Run(bot)
start = Start(bot)
buy_ticket = Buy_Ticket(bot)

@bot.message_handler(commands=["run"])  
def handle_run_command(message):
    run_text.Runs(message)

@bot.message_handler(commands=["start"])
def handle_start_command(message):
    start.ST(message)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    if call.data == "YES":
        new_condition = {"$set": {"text_Condition": run_text.Text_Conditions}}
        document.update_one({}, new_condition)
        bot.send_message(call.message.chat.id, "✅Розигриш запустився")
    elif call.data == "NO":
        run_text.Conditions(call.message)
    elif call.data == "btn_buy_Tickets": 
        buy_ticket.Buy(call.message)
    elif call.data == "btn_plus":
        buy_ticket.sum_Tickets += 1
        buy_ticket.sum_number += 100
        buy_ticket.update_sum_button()
    elif call.data == "btn_minus":
        buy_ticket.sum_Tickets -= 1 
        buy_ticket.sum_number -= 100
        buy_ticket.minus_undate_sum_button()
    elif call.data == "btn_result":
        buy_ticket.Payment(call.message)


bot.polling(non_stop=True)
