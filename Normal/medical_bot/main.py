import telebot

from cogs.Start import Start

bot = telebot.TeleBot("6740909089:AAFsHKxhG0YXTSBXG1RJStcp8SdIxyavhUw")

starts = Start(bot)

@bot.message_handler(commands=["start"])
def start(message):
    starts.start(message.chat.id)


@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    if call.data == "about_us":
        bot.send_message(call.message.chat.id, "")

bot.polling(non_stop=True)