# -*- coding: utf-8 -*-
import telebot
from telebot import types

TOKEN = ''
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands = ['start'])
def start(message):
    try:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        btn1 = types.KeyboardButton("Order delivery") #Заказать доставку пиццы
        markup.add(btn1)
        bot.send_message(message.chat.id, '<b>Привет. Я бот для заказа пиццы!</b>', parse_mode='html',
                         reply_markup=markup)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так...')

@bot.message_handler(content_types=['text'])
def menu(message):
    try:
        get_message_bot = message.text.strip().lower()
        if get_message_bot == "order delivery": #Заказать доставку пиццы
            markup = types.ReplyKeyboardMarkup(True, one_time_keyboard=True, row_width=2)
            btn1 = types.KeyboardButton('Margarita')#Маргарита
            btn2 = types.KeyboardButton('Diabola')#Диабола
            btn3 = types.KeyboardButton('Cizillian')#Сицилийская
            btn4 = types.KeyboardButton('Havayian')#Гавайская
            btn5 = types.KeyboardButton('Neopolitan')#По-неаполитански
            btn6 = types.KeyboardButton('4 cheeses')#Четыре сыра
            markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
            send_mess = "<b>Выберите Вашу пиццу</b>"
            bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)
            bot.register_next_step_handler(message, askname)
            markup = types.ReplyKeyboardHide(selective=False)

    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так...')

def askname(message):
    try:
        #markup = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id, "<b>ФИО заказчика\nIvanov Ivan Ivanovich</b>", parse_mode='html')
        #user_info['username'] = message.text
        bot.register_next_step_handler(message, askgeo)
        #markup = types.ReplyKeyboardHide()#selective=False)

    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так...')

def askgeo(message):
    try:
        keyboard = types.ReplyKeyboardMarkup(True, one_time_keyboard=True)
        button_geo = types.KeyboardButton(text="send location", request_location=True)
        keyboard.add(button_geo)
        bot.send_message(message.chat.id, "<b>Укажите место доставки. Напишите адрес или отправьте геопозицию</b>",
                         parse_mode='html', reply_markup=keyboard)
        bot.register_next_step_handler(message, asktime)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так...')

def asktime(message):
    try:
        bot.send_message(message.chat.id, "<b>Укажите удобное вермя для доставки:</b>", parse_mode='html')
        bot.register_next_step_handler(message, askphone)

    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так...')


def askphone(message):
    try:
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        button_phone = types.KeyboardButton(text="send phone number", request_contact=True)
        keyboard.add(button_phone)
        bot.send_message(message.chat.id, "<b>Отправьте свой номер телефона</b>", parse_mode='html', reply_markup=keyboard)
        markup = types.ReplyKeyboardHide(selective=False)
        bot.register_next_step_handler(message, checkorder)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так...')

def checkorder(message):
    try:
        bot.send_message(message.chat.id, "<b>Заказ принят в обработку. Мы перезвоним Вам для уточнения заказа. "
                                          "Списибо.</b>", parse_mode='html')
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так...')


bot.polling()