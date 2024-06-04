import telebot
from telebot import types


class Stop():
    def __init__(self, bot, status = "Вкл."):
        self.bot = bot
        self.status = status


    def Stop_def(self, message):
        markup = types.InlineKeyboardMarkup()
        Stop_btn = types.InlineKeyboardButton(text = "Зупинити", callback_data = "Stop_btn")
        Exit_button_Stop = types.InlineKeyboardButton(text = "Назад", callback_data = "Exit_button_Stop")

        markup.row(Stop_btn)
        markup.row(Exit_button_Stop)
        self.bot.send_message(message.chat.id, f"⛔<b>Ця функція дозволяє Вам на час приостановити подписку на ваш канал. В цьому випадку заявки ботом більше не будть приніматися і бот більше не буде принімати і бот більше не буде придлагати купити підписку на ваш канал</b>\n\n<b><u>Статус</u></b>: {self.status}", parse_mode = "HTML", reply_markup = markup)

    def Update_Stop_On(self, message):
        try:
            new_text = f"⛔<b>Ця функція дозволяє Вам на час приостановити подписку на ваш канал. В цьому випадку заявки ботом більше не будть приніматися і бот більше не буде принімати і бот більше не буде придлагати купити підписку на ваш канал</b>\n\n<b><u>Статус</u></b>: {self.status}"

            update_markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Включити", callback_data = "On")).add(types.InlineKeyboardButton("Назад", callback_data = "Exit_Stop"))

            self.bot.send_message(message.chat.id, new_text, parse_mode="HTML", reply_markup = update_markup)
        except:
            self.bot.send_message(message.chat.id, "Помилка не вдалося відключити!")

    def Update_Stop_off(self, message):
        try:
            new_text = f"⛔<b>Ця функція дозволяє Вам на час приостановити подписку на ваш канал. В цьому випадку заявки ботом більше не будть приніматися і бот більше не буде принімати і бот більше не буде придлагати купити підписку на ваш канал</b>\n\n<b><u>Статус</u></b>: {self.status}"
            undate_merkup  = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Виключити"))
        except:
            self.bot.send_message(message.chat.id, "Помилка!\n\nНе вдалося включити опцію!")