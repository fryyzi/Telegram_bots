import telebot
from telebot import types

# Ваш токен бота
TOKEN = '6740909089:AAFsHKxhG0YXTSBXG1RJStcp8SdIxyavhUw'

# Створення об'єкту бота
bot = telebot.TeleBot(TOKEN)

# ID або username вашого каналу
CHANNEL_ID = '@ФОБІЯ 18+'

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привіт! Надішліть команду /subscribers, щоб дізнатися кількість підписників на каналі.")

@bot.message_handler(commands=['subscribers'])
def get_subscribers(message):
    try:
        chat = bot.get_chat(CHANNEL_ID)
        print(message)
        members_count = chat.get('members_count', 'Невідомо')
        bot.reply_to(message, f"Кількість підписників на каналі: {members_count}")
    except Exception as e:
        bot.reply_to(message, f"Не вдалося отримати кількість підписників: {e}")

# Запуск бота
bot.polling()
