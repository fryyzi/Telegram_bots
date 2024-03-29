import tkinter as tk
from tkinter import filedialog
from pymongo import MongoClient

connect = MongoClient("mongodb://localhost:27017")
db = connect["Film_bot"]
document = db["info_film"]
number_document = db["last_number"]


def update_last_number_label():
    last_number_doc = number_document.find_one(sort=[("Число", -1)])  
    last_number = last_number_doc["Число"] if last_number_doc else "Немає даних"
    last_number_label.config(text=f"Останній номер фільму: {last_number}")

def add_film():
    global last_number_label

    number = int(number_Button_var.get())
    if number_document.count_documents({"Число": number}) > 0:
        print("Такий номер вже є")
        return

    film_data = {
        "Назва фільма": Entry_name_film_var.get(),
        "Райтинг фільма": Entry_raiting_film_var.get(),
        "Опис фільма": Entry_description_film_var.get(),
        "Картінка": image_patch if 'image_patch' in globals() else "Не вибрано",  # Перевірка чи було вибрано зображення
    }
    document.insert_one(film_data)

    last_number = {
        "Назва фільма": Entry_name_film_var.get(),
        "Число": number
    }
    number_document.insert_one(last_number)

    print("Фільм додано")
    update_last_number_label()

def choose_image():
    global image_patch
    file_patch = filedialog.askopenfilename()
    image_patch = file_patch

window = tk.Tk()
window.title("Add database")
window.geometry("720x250")

#name film
name_film = tk.Label(window, text="Назва фільма", foreground="red")
name_film.place(x=0, y=0)
Entry_name_film_var = tk.StringVar()
name_film_Entry = tk.Entry(textvariable=Entry_name_film_var)
name_film_Entry.place(x=0, y=15)

#raiting film
raiting_film = tk.Label(window, text="Рейтинг", foreground="red")
raiting_film.place(x=0, y=50)
Entry_raiting_film_var = tk.StringVar()
raiting_film_entry = tk.Entry(textvariable=Entry_raiting_film_var)
raiting_film_entry.place(x=0, y=65)

#description film
description_film = tk.Label(window, text="Опис фільма", foreground="red")
description_film.place(x=0, y=90)
Entry_description_film_var = tk.StringVar()
description_film_Entry = tk.Entry(textvariable=Entry_description_film_var)
description_film_Entry.place(x=0, y=105)

#film number
number_lbl = tk.Label(window, text="Номер фільму", foreground="red")
number_lbl.place(x=0, y=130)
number_Button_var = tk.StringVar()
number_Button = tk.Entry(textvariable=number_Button_var)
number_Button.place(x=0, y=155)

# Останній номер фільму
last_number_label = tk.Label(window, text="Останній номер фільму: ")
last_number_label.place(x=300, y=0)

Button_choose_image = tk.Button(window, width=20, text="Вибрати зображення", command=choose_image)
Button_choose_image.place(x=0, y=180)

Button_add = tk.Button(window, width=20, text="Додати фільм", command=add_film)
Button_add.place(x=0, y=200)

last_number_label = tk.Label(window, text="Останній номер фільму: ")
last_number_label.place(x=300, y=0)
update_last_number_label()  # Викликаємо при старті, щоб показати актуальний останній номер


window.mainloop()

#зробити нове відобраенря оставнього числа