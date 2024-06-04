import telebot

bot = telebot.TeleBot("6271631030:AAE50Ty4Aib5xvRlTCh20dXxo-p6E7PrTPg")

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "test")


bot.polling(non_stop=True)