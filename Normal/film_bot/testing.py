from bs4 import BeautifulSoup as BS
import requests

url = 'https://m.kinoafisha.ua'
response = requests.get(url)
soup = BS(response.text, "lxml")

film_block = soup.find("div", class_="snowContainer")


