import telebot
from telebot import types

bot = telebot.TeleBot('7091823434:AAF3ay1obap2-F__jXBkmrc_gf4D6yR2LLY')


@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("✔️ Узнать курс")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn2 = types.KeyboardButton("О нас")
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, " 😁 Здравствуйте! ", reply_markup=markup) #  mass - str сообщеня 

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print(message)
    if message.text == '✔️ Узнать курс':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
       
        btn1 = types.KeyboardButton('$ Доллар')
        btn2 = types.KeyboardButton('€ Евро')
        btn3 = types.KeyboardButton('¥ Юань')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '$ € ¥ Выберите валюту!', reply_markup=markup) #ответ бота
    
    if message.text == 'О нас':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
       
        btn1 = types.KeyboardButton('Наш сайт')
        btn2 = types.KeyboardButton('Сколько мы уже говорим все о курсе')
        btn3 = types.KeyboardButton('Кто создатель')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, 'Информация о нас!', reply_markup=markup) #ответ бота

    elif message.text == 'Наш сайт':
        bot.send_message(message.from_user.id, '[Сюда](https://www.cbr.ru/)', parse_mode='Markdown')

    elif message.text == 'Сколько мы уже говорим все о курсе':
        bot.send_photo(message.from_user.id, 'https://files5-cdn.slide-life.ru/cards/9/7/c/e/6/yarkaya-otkrytka-s-dnem-rozhdeniya-devushke-25-let.webp')

    elif message.text == 'Кто создатель':
        bot.send_message(message.from_user.id, 'Митя Фомен')

    elif message.text == '$ Доллар':
        bot.send_message(message.from_user.id, '1 USD = 92.50 RUB ' + '[Узнать на сайте](https://www.cbr.ru/currency_base/daily/)', parse_mode='Markdown')

    elif message.text == '€ Евро':
        bot.send_message(message.from_user.id, '1 EUR = 100.10 RUB ' + '[Узнать на сайте](https://www.cbr.ru/currency_base/daily/)', parse_mode='Markdown')

    elif message.text == '¥ Юань':
        bot.send_message(message.from_user.id, '1 CNY = 12.78 RUB ' + '[Узнать на сайте](https://www.cbr.ru/currency_base/daily/)', parse_mode='Markdown')


bot.polling(none_stop=True, interval=0) 