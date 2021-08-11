import telebot

bot = telebot.TeleBot("1840495085:AAHB_rJZidAqGygWQEGie-B4uhGH6Cu3wt8")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "I can do calculations, type expression")


@bot.message_handler(func=lambda message: True)
def send_welcome(message):
    '''
    a, op, b = message.text.split()
    a, b = float(a), float(b)
    res = 0
    if op == '+':
        res = a + b
    elif op == '-':
        res = a - b
    '''
    bot.reply_to(message, eval(message.text))


bot.polling()