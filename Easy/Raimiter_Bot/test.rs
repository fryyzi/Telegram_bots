extern crate gtk;
extern crate glib;

use gtk::prelude::*;
use gtk::{Button, Window, WindowType};

fn main() {
    // Ініціалізація GTK
    gtk::init().expect("Failed to initialize GTK.");

    // Створення нового вікна
    let window = Window::new(WindowType::Toplevel);
    window.set_title("Простий приклад GTK");
    window.set_default_size(350, 70);

    // Створення нової кнопки
    let button = Button::new_with_label("Натисни мене!");

    // Додавання події при натисканні на кнопку
    button.connect_clicked(|_| {
        println!("Кнопка натиснута!");
    });

    // Додавання кнопки до вікна
    window.add(&button);

    // Показати всі віджети у вікні
    window.show_all();

    // Обробка закриття вікна
    window.connect_delete_event(|_, _| {
        gtk::main_quit();
        Inhibit(false)
    });

    // Запуск основного циклу GTK
    gtk::main();
}
