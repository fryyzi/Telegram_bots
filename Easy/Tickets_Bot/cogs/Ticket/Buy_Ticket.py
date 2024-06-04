from telebot import types

class Buy_Ticket():
    def __init__(self, bot, sum_Tickets = 0, sum_number = 0):
        self.bot = bot
        self.sum_Tickets = sum_Tickets
        self.sum_number = sum_number
        self.chat_id = None  # Доданий атрибут для зберігання chat_id
        self.message_id = None  # Доданий атрибут для зберігання message_id

    def Buy(self, message):
        self.chat_id = message.chat.id
        marcup = types.InlineKeyboardMarkup()
        btn_plus = types.InlineKeyboardButton(text="➕", callback_data="btn_plus")
        btn_minus = types.InlineKeyboardButton(text="➖", callback_data="btn_minus")
        btn_sum_Tickets = types.InlineKeyboardButton(text=self.sum_Tickets, callback_data="btn_sum")
        non_button = types.InlineKeyboardButton(text = "Оплата не доступна", callback_data = "non_button")
        btn_sum_number = types.InlineKeyboardButton(text=f"Обща сумма {self.sum_number} грн",
                                                    callback_data="btn_sum_number")
        btn_exit = types.InlineKeyboardButton(text="Назад", callback_data="btn_exit")

        marcup.row(btn_plus, btn_sum_Tickets, btn_minus)
        marcup.row(btn_sum_number)
        marcup.row(non_button)
        marcup.row(btn_exit)
        
        sent_message = self.bot.send_message(message.chat.id,
                                             "Тут ви можете купити додаткові білети для збільшення шансів на виграш\n1<b>билет = 100грн</b>\nВикористовуйте кнопки ниже щоб купити білети\n❗Кнопка по середині покажує скількість білетів яку ви купили",
                                             parse_mode="HTML",
                                             reply_markup=marcup)
        self.message_id = sent_message.message_id 
        return sent_message

    def update_sum_button(self):
        new_text = self.sum_Tickets 
        marcup = types.InlineKeyboardMarkup()
        btn_sum_Tickets = types.InlineKeyboardButton(text=new_text, callback_data="btn_sum")
        btn_sum_number = types.InlineKeyboardButton(text=f"Обща сумма {self.sum_number} грн",
                                                    callback_data="btn_sum_number")
        btn_plus = types.InlineKeyboardButton(text="➕", callback_data="btn_plus")
        btn_minus = types.InlineKeyboardButton(text="➖", callback_data="btn_minus")
        btn_result = types.InlineKeyboardButton(text="Перейти к оплате", callback_data="btn_result")
        btn_exit = types.InlineKeyboardButton(text="Назад", callback_data="btn_exit")

        marcup.row(btn_plus, btn_sum_Tickets, btn_minus)
        marcup.row(btn_sum_number)
        marcup.row(btn_result)
        marcup.row(btn_exit)
    
        # Редагуємо повідомлення з оновленою клавіатурою
        self.bot.edit_message_reply_markup(chat_id=self.chat_id,
                                            message_id=self.message_id,
                                            reply_markup=marcup)


    def minus_undate_sum_button(self):
        new_text = self.sum_Tickets  # Отримуємо новий текст для кнопки btn_sum
        # Оновлюємо текст кнопки "btn_sum"
        marcup = types.InlineKeyboardMarkup()
        btn_sum_Tickets = types.InlineKeyboardButton(text=new_text, callback_data="btn_sum")
        btn_sum_number = types.InlineKeyboardButton(text=f"Обща сумма {self.sum_number} грн",
                                                    callback_data="btn_sum_number")
        btn_plus = types.InlineKeyboardButton(text="➕", callback_data="btn_plus")
        btn_minus = types.InlineKeyboardButton(text="➖", callback_data="btn_minus")
        non_button = types.InlineKeyboardButton(text = "Оплата не доступна", callback_data = "non_button")
        btn_result = types.InlineKeyboardButton(text="Перейти к оплате", callback_data="btn_result")
        btn_exit = types.InlineKeyboardButton(text="Назад", callback_data="btn_exit")

        marcup.row(btn_plus, btn_sum_Tickets, btn_minus)
        marcup.row(btn_sum_number)
        if self.sum_number > 0:
            marcup.row(btn_result)
        if self.sum_number == 0:
            marcup.row(non_button)
        marcup.row(btn_exit)
    
        self.bot.edit_message_reply_markup(chat_id=self.chat_id,
                                            message_id=self.message_id,
                                            reply_markup=marcup)
        

    def Payment(self, message):
        marckup = types.InlineKeyboardMarkup()
        btn_payment = types.InlineKeyboardButton(text = "Оплата", callback_data = "btn_payment")
        btn_exit_payment = types.InlineKeyboardButton(text = "Назад", callback_data = "btn_exit_payment")
        marckup.row(btn_payment)
        marckup.row(btn_exit_payment)
        self.bot.send_message(message.chat.id, f"<b>Вибрано білетів</b>: {self.sum_Tickets}\n<b>Обща сумма оплати</b>: {self.sum_number}\n Оплатіть сумму перейдя по кнопці ниже і бот автоматично зачислить на Ваш счьот в текущем розигріші колекцію", parse_mode = "HTML", reply_markup=marckup)