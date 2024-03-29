import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup as BS
from pymongo import MongoClient


bot = telebot.TeleBot("6751068161:AAEMmMxizBGaqj96IZh0xOYBQw4uhQyhvoo")

# Підключення до бази даних MongoDB
client = MongoClient('localhost', 27017)
db = client['photos_database']
photos_collection = db['photos']

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 'Добро пожаловать в телеграм бот де ви зможете знайти найкращі фільми по жанрам\nПросто натисніть на кнопку жанра якого фільма ви хочете знайти')
    

@bot.message_handler(commands=["top"])
def top(message):
    pass  # Ваша логіка тут

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    file_id = message.photo[-1].file_id
    photo_info = {
        'file_id': file_id,
        'chat_id': message.chat.id,
        'message_id': message.message_id
    }
    photos_collection.insert_one(photo_info)
    bot.reply_to(message, 'Фото збережено')

@bot.message_handler(commands=["test"])
def test(message):
    cursor = photos_collection.find()
    for res in cursor:
        photo = res.get("file_id")

        bot.send_photo(message.chat.id, photo=photo)


@bot.message_handler(commands=['testing'])
def testing(message):
    url = 'https://m.kinoafisha.ua'
    response = requests.get(url)
    soup = BS(response.text, "lxml")

    subcategories = soup.find("div", "row")
    



bot.polling(non_stop=True)