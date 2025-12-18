
import telebot
from telebot import types
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = "8217951972:AAEMFf-UsMEdvrQohlNlmTYYzPgvfD8nro4" #TRON
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f"privet! Vvidi /menu chat yvedit knopki.'")


@bot.message_handler(commands=['menu'])
def menu(message):

    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(types.KeyboardButton("https://youtu.be/iIXWtBSZ1ps?si=oog10CvH1hlzc3od"),
types.KeyboardButton("ne najemai"))
    kb.add(types.KeyboardButton("https://www.google.com"))
    kb.add(types.KeyboardButton("https://www.Music.youtube.com")) 
    kb.add(types.KeyboardButton("https://www.deepseek.com/en"))
    kb.add(types.KeyboardButton("https://kinogo.ps/"))
    kb.add(types.KeyboardButton("https://t.me/Lacoste_m1"))
    bot.send_message(message.chat.id,"menu:",
                     reply_markup=kb)
    

@bot.message_handler(func=lambda message:True)
def handler_text(message):
    t = (message.text or"").strip().lower()

    if t == "Pomosh".lower():
        bot.send_message(message.chat.id, "eto razdel pomoshi. Komandy /start/help/menu//inline/whoami")
    elif t == "pozdorovatysya".lower():
        first= message.from_user.first_name or "frend"
        bot.send_message(message.chat.id, f"privet,hello,{first}!")
    elif t == "Skrut klaviatyru".lower():
        hide=types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id,"klaviatyra ",
                         reply_markup=hide)
    else:
        bot.send_message(message.chat.id,"YA ne ponimau tebya,NAPSHI ya durak")



print("Bot zapushen")
bot.polling(none_stop=True)