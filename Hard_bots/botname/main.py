import telebot
from telebot import types
import pymongo

from cogs.start import CommandHandler
from cogs.Withdraw import Withdraw
from cogs.admin import Admin
from cogs.add_balanse import Add_balanse
from cogs.help.help import Help
from cogs.Subcribes.Subcribes import Subcribes
from cogs.Approve.Approve import Approve
from cogs.Author.Author import Author
from cogs.Channel.Channel import Channel
from cogs.Channel_Setting.Message.Message import Message
from cogs.Channel_Setting.Stop.Stop import Stop
from cogs.Channel_Setting.strict_regime.strict import Strict
from cogs.WhileLIst.WhileList import WhileList


bot = telebot.TeleBot("6271631030:AAE50Ty4Aib5xvRlTCh20dXxo-p6E7PrTPg")
connect = pymongo.MongoClient("mongodb://localhost:27017")
db = connect["botname"]
Withdraw_collection = db["Withdraw"]
User_collection = db["User"]
Helps = db["Help_text"]

handler = CommandHandler(bot)
withdraw_instance = Withdraw(bot)
admins = Admin(bot)
add_balanse = Add_balanse(bot)
help = Help(bot)
Sub = Subcribes(bot)
approve = Approve(bot)
author = Author(bot)
channel = Channel(bot)
message_class = Message(bot)
stop = Stop(bot)
strict = Strict(bot)
W_list = WhileList(bot)


number = 1
number_balanse = 100
global User_id_chat
CommandHandler

def handle_cart_request(message):
    bot.register_next_step_handler(message.chat.id, process_car_amount)

def process_car_amount(message):
    marcup = types.InlineKeyboardMarkup()
    exit_balanse = types.InlineKeyboardButton(text="⬅️Назад",  callback_data="exit_balanse_card")
    marcup.add(exit_balanse)
    bot.send_message(message.chat.id, f"<b>Шаг {number + 1} / 2</b>\n\nПришлите номер карты, куда соввершится вывод средств:\n\n<b>Пример</b>: 5454 5454 5454 5454", reply_markup=marcup, parse_mode="HTML")
    bot.register_next_step_handler(message, text)
        
@bot.message_handler(func=lambda message: True, content_types=['new_chat_members'])
def new_member(message):
    if message_class.new_persone_status == "Вкл":
        try:
            chat_id = message.chat.id
            bot.send_message(chat_id, f"Ласкаво просимо до групи, @{message.from_user.username}!")
        except:
            bot.send_message(chat_id, "Помилка, не вдалося розпізнати користувача!")

def text(message):
    number_card = int(message.text)
    try:
        bot.send_message(message.chat.id, "Ваша заявка переданна в обработку.\nКак только Ваши срудства будут выведены из бота, Вы получите уведовление")

        add_Withdraw = {
            "Name": message.chat.first_name,
            "number_card": number_card,
            "balanse": amount,
            "id_channel": message.from_user.id,
        } 
        Withdraw_collection.insert_one(add_Withdraw)

    except ValueError:
        bot.send_message(message.chat.id, "❌Неверный формат ввода карты\n<b>Пример</b> 5454 5454 5454 5454\n<b>Попробуйте ввести снова:</b>", parse_mode="HTML")
        handle_cart_request(message, process_car_amount)

def handle_withdraw_request(call):
    bot.register_next_step_handler(call.message, process_withdraw_amount)

def process_withdraw_amount(message):
    try:
        global amount
        amount = int(message.text)
        if amount <= number_balanse:
            process_car_amount(message)
        if amount > number_balanse:
            bot.send_message(message.chat.id, "❌На вашем балансе менше, чем Вы ввели. <b>Попробуйте ввести снова:</b>", parse_mode="HTML")
            bot.register_next_step_handler(message, process_withdraw_amount)
    except ValueError:
        bot.send_message(message.chat.id, "❌ Сумма должна состоять из цифр. Попробуйте ввести снова.", parse_mode="HTML")
        bot.register_next_step_handler(message, process_withdraw_amount)

    

@bot.message_handler(commands=['start'])
def handle_start(message):
    handler.handle_start(message)


@bot.message_handler(commands=["aprrove"])
def Aprrove(message):
    approve.App(message)


@bot.callback_query_handler(func=lambda call: True)
def handle_call(call):
    if call.data == "Balance":
        withdraw_instance.dalanse(call.message)
    elif call.data == "Withdraw":
        marcup = types.InlineKeyboardMarkup()
        exit_balanse = types.InlineKeyboardButton(text="⬅️Назад",  callback_data="exit_balanse_money")
        marcup.row(exit_balanse)
        bot.send_message(call.message.chat.id, f"<b>Шаг {number} / 2</b>\n\nВпишите сумму в рублях, для вывода\n<i>(Используя только цифры)</i>:", reply_markup=marcup, parse_mode="HTML")
        handle_withdraw_request(call)
    elif call.data == "exit_main_menu":
        handler.handle_start(call.message)
    if call.data == "Add_admin":
        bot.send_message(call.message.chat.id, "text")

    if call.data == "exit_balanse_money":
        handler.handle_start(call.message)
    if call.data == "exit_balanse_card":
        handler.handle_start(call.message)
    if call.data == "Withdeaw_admin":
        Complited_Markup = types.InlineKeyboardMarkup()
        Complited_Button = types.InlineKeyboardButton("✅ Одобрить", callback_data = "Complited")
        Refuse_Button = types.InlineKeyboardButton("❌ Отклонить", callback_data = "Refuse")
        Complited_Markup.row(Complited_Button, Refuse_Button)
        cursore = Withdraw_collection.find()
        for res in cursore:
            User_Name = res.get("Name")
            User_Number_card = res.get("number_card")
            User_balanse = res.get("balanse")
            User_id_chat = res.get("id_channel")
            bot.send_message(call.message.chat.id, f"➖<b>Новая заявка на вывод</b>➖\n<b>Сумма вывода: </b>{User_balanse}\n<b>Реквизиты: </b>{User_Number_card}\n<b>Пользоатель: </b>{User_Name}", reply_markup=Complited_Markup, parse_mode="HTML")

    if call.data == "Admin_Help_Menu":
        cursore = Helps.find()

        for res in cursore:
            Name = res.get("Name")
            Help_Text = res.get("Text")
            User_Name = res.get("User_Name")
            bot.send_message(call.message.chat.id, f"❗Потрібна нова помочь❗\nВід: {Name}\nТекст: {Help_Text}\nАкаунт: {User_Name}") 

    if call.data == "Complited":
        cursore = Withdraw_collection.find()
        for res in cursore:
            User_id_chat = res.get("id_channel")
            User_Name = res.get("Name")
            User_Number_card = res.get("number_card")
            User_balanse = res.get("balanse")
            id = User_id_chat
            bot.send_message(id, f"<b>✅Ваша заявка на вивод средтв в размере</b>\n{User_balanse} Руб успешно обработана и переведена по карте {User_Number_card}", parse_mode="HTML")
        
    if call.data == "Refuse":
        cursore = Withdraw_collection.find()
        for res in cursore:
            User_id_chat = res.get("id_channel")
            User_Name = res.get("Name")
            User_Number_card = res.get("number_card")
            User_balanse = res.get("balanse")
            id = User_id_chat
        bot.send_message(id, f"<b>❌Ваша заявка на вывод средств в размере</b> {User_balanse} Руб отключена\nСвяжитесь с администраторами по кнопке '🍰Поддержка' что бы выснить причину", parse_mode="HTML")    
    
    if call.data == "pay_pay":
        bot.send_message(call.message.chat.id, "ТУТ ДОЛЖНО БЫТЬ ССЫЛКА НА РЕКВИЗИТЫ")
    if call.data == "add_balanse":
        add_balanse.add_balanse_call(call.message)
    if call.data == "add_balanse_admin":
        admins.process_balanse_amount(call.message)
    if call.data == "Support":
        help.Help_menu(call.message)
    if call.data == "Sapport_button":
        help.Complited(call.message)
    if call.data == "Exit_Chat_Button":
        bot.send_message(call.message.chat.id, text = "Ваша розмова закрита!")




    if call.data == "Subscriptions":
        Sub.Sub(call.message)
    if call.data == "Create_Sub":
        Sub.Create(call.message)
    if call.data == "Channel":
        Sub.Channel(call.message)

    if call.data == "Author":
        author.Author(call.message)

    if call.data == "test":
        channel.Channel_main(call.message)
    if call.data == "Message":
        message_class.Message(call.message)

    if call.data == "New_Persone":
        message_class.new_persone_status = "Викл."
        message_class.Update_Persone(call.message)
    if call.data == "Exit_New_Persone":
        message_class.Message(call.message)
    if call.data == "New_commment":
        message_class.new_commentar_status = "Викл."
        message_class.Unpdate_Commnets(call.message)
    if call.data == "Report":
        message_class.new_report_status = "Викл."
        message_class.Update_Report(call.message)
    if call.data == "Stop":
        stop.Stop_def(call.message)
    if call.data == "Stop_btn":
        stop.status = 'Викл.'
        stop.Update_Stop_On(call.message)
    if call.data == "On":
        stop.status = "Вкл."
        stop.Stop_def(call.message)        
    if call.data == "Strict_Controle":
        strict.Strict_def(call.message)
    if call.data == "On_btn":
        strict.status = "Вкл"
        strict.Update_Button(call.message)
    if call.data == "On_stri":
        strict.status = "Викл"
        strict.Strict_def(call.message)
    if call.data == "Edit_money":
        channel.Price(call.message)
    if call.data == "Edit_WhileList":
        W_list.While_List_Menu(call.message)



@bot.message_handler(commands=['admin'])
def admin(message):
    admins.admin(message)

bot.polling(non_stop=True)