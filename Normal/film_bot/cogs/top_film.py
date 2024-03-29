import requests
from bs4 import BeautifulSoup as BS

class top_film:
    def __init__(self, url):
        self.url = url


    def test(self, url):
        urls = url
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