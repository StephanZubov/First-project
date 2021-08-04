# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.

import telebot

bot = telebot.TeleBot("1840495085:AAHB_rJZidAqGygWQEGie-B4uhGH6Cu3wt8")
setattr(bot, 'state', 'main_menu')
setattr(bot, 'memory', {})


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


# bot.reply_to(message, message.text)
def reg_name(message):
    global name
    name = message.text


@bot.message_handler(func=lambda message: bot.state == 'main_menu')
def echo_all(message):
    if message.from_user.id not in bot.memory:
        bot.memory[message.from_user.id] = {}

    if message.text == 'Привет':
        bot.reply_to(message, 'Привет создатель бота!')
    elif message.text == 'Hello':
        bot.reply_to(message, 'Hello, sir!')
    elif message.text == '/reg':
        bot.send_message(message.from_user.id, 'Привет. Давай познакомимся. Как тебя зовут?')
        bot.state = 'info_wait'


@bot.message_handler(func=lambda message: bot.state == 'info_wait')
def register_name(message):
    bot.memory[message.from_user.id]['name'] = message.text
    bot.send_message(message.from_user.id, f'Приятно познакомится, {message.text}')
    bot.state = 'main_menu'


def reg_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, reg_age)


def reg_age(message):
    global age
    # age = message.text
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Вводите цифрами!')

bot.polling()