import telebot
from telebot import types


class Subcribes():
    def __init__(self, bot):
        self.bot = bot

    def Sub(self, message):
        Sub_Marcup = types.InlineKeyboardMarkup()
        Create_Sub = types.InlineKeyboardButton(text = "⚒️Створити", callback_data="Create_Sub")
        Author = types.InlineKeyboardButton(text = "🙎Автор", callback_data = "Author")
        Sub = types.InlineKeyboardButton(text = "📜Підпписник", callback_data = "Sub")
        Exit = types.InlineKeyboardButton(text = "⬅️Назад", callback_data = "Exit")

        Sub_Marcup.row(Create_Sub)
        Sub_Marcup.row(Author, Sub)
        Sub_Marcup.row(Exit)

        self.bot.send_message(message.chat.id, 
                              text = "☀️Викорстовуючи це меню ви можете управляти функціоналом платних підписок\n\n🖋️Будучи <b>автором</b> Ви зможете створювати і редеактірвать свою підписку встановлюючи їй ціню\n\n📅З позиції <b>підпискника</b> підтримувати любімий контент контейтмейкерів, абоо же управляти своєю підпискую\n\n💰Підписка продлевається автоматично з вашаго балансаБ при цьому всі неплатіжники відсліджуються і удаляються автоматично самим ботом що дуже удобно і справедліво", reply_markup = Sub_Marcup, parse_mode = "HTML")
        

    def Create(self, message):
        Create_Marcup = types.InlineKeyboardMarkup()
        Channel = types.InlineKeyboardButton(text = "Канал", callback_data = "Channel")
        Group = types.InlineKeyboardButton(text = "Группа", callback_data = "Group")
        Exit = types.InlineKeyboardButton(text = "Назад", callback_data = "Exit")

        Create_Marcup.row(Channel, Group)
        Create_Marcup.row(Exit)

        self.bot.send_message(message.chat.id, text = "👇Виберіть тип чата який хочете створити", reply_markup = Create_Marcup)

    def Channel(self, message):
        Channel_Marcup = types.InlineKeyboardMarkup()
        Information = types.InlineKeyboardButton(text = "❓Дод. Інформація", callback_data = "Information")
        Create_Channel = types.InlineKeyboardButton(text = "➕Створити канал", callback_data = "Create_Channel")
        Exit_channel = types.InlineKeyboardButton(text = "⬅️Назад", callback_data = "Exit_channel")


        Channel_Marcup.row(Information, Create_Channel)
        Channel_Marcup.row(Exit_channel)

        self.bot.send_message(message.chat.id, text = "❓Якщо ви хочете створити підписку на Ваш канал то:\n\nКанал повинен будти закритий\nДайте боту наступні права адміністратора\nПраво на додавання нових учасників\nГотово", reply_markup = Channel_Marcup, parse_mode = "HTML")
    
    def Group(self, message):
        Group_Marcup = types.InlineKeyboardMarkup()
        Info = types.InlineKeyboardButton(text = "❓Дод. Інформація", callback_data = "Info")
        Create_group = types.InlineKeyboardButton(text = "➕Створити Групу", callback_data = "Create_group")
        Exit = types.InlineKeyboardButton(text = "⬅️Назад", callback_data = "Exit")

        Group_Marcup.row(Info, Create_group)
        Group_Marcup.row(Exit)

        self.bot.send_message(message.chat.id, text = "❓Якщо ви хочете створити створити платну  підписку на Вашу группу то:\n\nДобавте в неї цього бота\nДайте ботові всі права Адміністратора, крім возможності добавляти нового адміністратора\nВведіть в группі командуу /approve")


