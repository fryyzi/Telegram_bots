import telebot

# from cogs.Author.Author import Author

# author = Author(bot = None)


class Approve():
    def __init__(self, bot = None):
        self.bot = bot
        self.channel = "test"

    def App(self, message):
        self.channel = message.chat.title
        self.bot.reply_to(message, f"Це повідомлення надіслано з каналу '{self.channel}'.")