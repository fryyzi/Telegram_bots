from telebot import types

class BotLogic:
    def __init__(self, bot):
        self.bot = bot
        self.markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    def create_button(self, message):
        try:
            # Отримуємо текст для кнопки з повідомлення користувача
            button_text = message.text

            # Створюємо нову кнопку
            button = types.KeyboardButton(button_text)

            # Додаємо нову кнопку до розмітки
            self.markup.add(button)

            # Відправляємо повідомлення з оновленою клавіатурою
            self.bot.send_message(message.chat.id, "Натисніть кнопку нижче:", reply_markup=self.markup)
        
        except Exception as e:
            print(f"Error: {e}")
            self.bot.send_message(message.chat.id, "Сталася помилка, спробуйте ще раз.")
