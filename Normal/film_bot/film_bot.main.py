import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup as BS
import pymongo
import base64

bot = telebot.TeleBot("6751068161:AAEMmMxizBGaqj96IZh0xOYBQw4uhQyhvoo")
connect = pymongo.MongoClient("mongodb://localhost:27017")
db = connect["Film_bot"]
document = db["info_film"]

@bot.message_handler(commands=["start"])
def start(message):
    show_main_menu(message.chat.id)

def show_main_menu(chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_one = types.KeyboardButton("Top")
    btn_search = types.KeyboardButton("Search")
    markup.add(btn_one, btn_search)
    bot.send_message(chat_id, "Виберіть топ фільмів або пошук", reply_markup=markup)


def search_film(message):
    bot.send_message(message.chat.id, "Введіть назву фільма")
    bot.register_next_step_handler(message, sell)

def sell(message):
    name_film = message.text
    cursor = document.find({"Назва фільма": name_film})
    for res in cursor:
        image_film = res.get("Картінка")
        Name_film = res.get("Назва фільма")
        reiting_film = res.get("Райтинг фільма")
        description_film = res.get("Опис фільма")

        if image_film:
            try:
                with open(image_film, 'rb') as file:
                    bot.send_photo(message.chat.id, file)
            except FileNotFoundError:
                bot.send_message(message.chat.id, f"Помилка: файл зображення '{image_film}' не знайдено.")
        
        message_text = f"Назва фільма: {Name_film}\nРейтинг фільма: {reiting_film}\nОпис фільма: {description_film}"
        bot.send_message(message.chat.id, message_text)


@bot.message_handler(content_types=["text"])
def top_film(message):
    if message.text == 'Top':
        marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bnt_animation = types.KeyboardButton("Анімація")
        btn_action = types.KeyboardButton("Бойовик")
        btn_childrens = types.KeyboardButton("Дитяче")
        btn_crime = types.KeyboardButton("Кримінал")
        btn_exit = types.KeyboardButton("Назад")
        
        marcup.add(bnt_animation, btn_action, btn_childrens, btn_crime, btn_exit)
        bot.send_message(message.chat.id, "Виберіть жанр", reply_markup=marcup)
        
    if message.text == "Search":
        search_film(message)

    if message.text == "Анімація":
        url = 'https://www.kinoafisha.info/rating/movies/animation/'
        response = requests.get(url)
        soup = BS(response.text, "lxml")

        subcategories = soup.find("div", class_="site_content")
        rating = subcategories.find("div", class_="ratings")
        rating_list = rating.find("div", class_="ratings_list")

        movies_list = rating_list.find_all("div", class_="movieList_item")

        full_message = ""

        for index, movie in enumerate(movies_list):
            if index < 5:
                info_film = movie.find("div", class_="movieItem_info")
                raiting_film = movie.find("span", class_="movieItem_itemRating")
    
                name_film = info_film.find("a", class_="movieItem_title")
                full_message += f"{name_film.text} - Рейтинг: {raiting_film.text}\n"
            else:
                break
        bot.send_message(message.chat.id, full_message)
    if message.text == "Бойовик":
        url = 'https://www.kinoafisha.info/rating/movies/action/'
        response = requests.get(url)
        soup = BS(response.text, "lxml")

        subcategories = soup.find("div", class_="site_content")
        rating = subcategories.find("div", class_="ratings")
        rating_list = rating.find("div", class_="ratings_list")

        movies_list = rating_list.find_all("div", class_="movieList_item")

        full_message = ""

        for index, movie in enumerate(movies_list):
            if index < 5:
                info_film = movie.find("div", class_="movieItem_info")
                raiting_film = movie.find("span", class_="movieItem_itemRating")
    
                name_film = info_film.find("a", class_="movieItem_title")
                full_message += f"{name_film.text} - Рейтинг: {raiting_film.text}\n"
            else:
                break
        bot.send_message(message.chat.id, full_message)
    if message.text == "Дитяче":
        url = 'https://www.kinoafisha.info/rating/movies/children/'
        response = requests.get(url)
        soup = BS(response.text, "lxml")

        subcategories = soup.find("div", class_="site_content")
        rating = subcategories.find("div", class_="ratings")
        rating_list = rating.find("div", class_="ratings_list")

        movies_list = rating_list.find_all("div", class_="movieList_item")

        full_message = ""

        for index, movie in enumerate(movies_list):
            if index < 5:
                info_film = movie.find("div", class_="movieItem_info")
                raiting_film = movie.find("span", class_="movieItem_itemRating")
    
                name_film = info_film.find("a", class_="movieItem_title")
                full_message += f"{name_film.text} - Рейтинг: {raiting_film.text}\n"
            else:
                break
        bot.send_message(message.chat.id, full_message)
    if message.text == "Кримінал":
        url = 'https://www.kinoafisha.info/rating/movies/criminal/'
        response = requests.get(url)
        soup = BS(response.text, "lxml")

        subcategories = soup.find("div", class_="site_content")
        rating = subcategories.find("div", class_="ratings")
        rating_list = rating.find("div", class_="ratings_list")

        movies_list = rating_list.find_all("div", class_="movieList_item")

        full_message = ""

        for index, movie in enumerate(movies_list):
            if index < 5:
                info_film = movie.find("div", class_="movieItem_info")
                raiting_film = movie.find("span", class_="movieItem_itemRating")
    
                name_film = info_film.find("a", class_="movieItem_title")
                full_message += f"{name_film.text} - Рейтинг: {raiting_film.text}\n"
            else:
                break
        bot.send_message(message.chat.id, full_message)

    if message.text == "Назад":
        show_main_menu(message.chat.id)


@bot.message_handler(commands=["search"])
def test(message):
    cursor = document.find()
    for res in cursor:
        image_film = res.get("Картінка")
        Name_film = res.get("Назва фільма")
        reiting_film = res.get("Райтинг фільма")
        description_film = res.get("Опис фільма")

        if image_film:
            try:
                with open(image_film, 'rb') as file:
                    bot.send_photo(message.chat.id, file)
            except FileNotFoundError:
                bot.send_message(message.chat.id, f"Помилка: файл зображення '{image_film}' не знайдено.")
        
        message_text = f"Назва фільма: {Name_film}\nРейтинг фільма: {reiting_film}\nОпис фільма: {description_film}"
        bot.send_message(message.chat.id, message_text)




@bot.message_handler(commands=["top"])
def test(message):
    if message.text == "test":
        bot.send_message(message.chat.id, "test")


bot.polling(non_stop=True)
