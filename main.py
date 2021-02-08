# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import telebot
bot = telebot.TeleBot('r')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Привет', 'Заказать')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуйте '+message.from_user.first_name+', вас приветствует бот компании Harzlabs, для просмотра списка основных команд отправьте мне /help', reply_markup=keyboard1)
#    print(message)

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'У нашего бота пока такие команды: \n /settings - получить настройки для принтеров \n заказать - эта команда отправит запрос нашему менеджеру и он в ближайшее время свяжется с Вами', reply_markup=keyboard1)
#    print(message)

@bot.message_handler(commands=['settings'])
def exchange_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Anet N4', callback_data='get-anetn4'),
        telebot.types.InlineKeyboardButton('Anycubic Photon', callback_data='get-anycubicphoton')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Asiga MAX', callback_data='get-asigamax'),
        telebot.types.InlineKeyboardButton('Anycubic Photon', callback_data='get-anycubicphoton')
    )

    bot.send_message(
        message.chat.id,
        'Выберете принтер:',
        reply_markup=keyboard
    )

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, '+message.from_user.last_name+' '+message.from_user.first_name)
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Пока, '+message.from_user.last_name+' '+message.from_user.first_name)
    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAM_X9wkPeF1ZMRosmuWjawGxrSZAaMAAnsBAAIJEjQAAeCjsVYVp7dUHgQ')
        bot.send_message(336893588, "кто-то любит бот")
    elif message.text.lower() == 'заказать':
        bot.send_message(message.chat.id, "С вами свяжутся в ближайшее время")
        bot.send_message(336893588, "@"+message.chat.username+' хочет сделать заказ, свяжитесь с ним')
        print(message)
    elif message.text.lower() == 'я сашуля':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAOgX9ycu_3sERw1_O_cbkhzI5n5t7EAAvsAA8wkbgPcaA0c65Z9-R4E')
        bot.send_voice(message.chat.id, 'AwACAgIAAxkBAAOqX9yfweIXGJLmMwIrAjY-nIzJ5SIAAmUJAAIK6OlK1kWktDIIOO8eBA')
    elif message.text.lower() == 'я саша':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAOgX9ycu_3sERw1_O_cbkhzI5n5t7EAAvsAA8wkbgPcaA0c65Z9-R4E')
        bot.send_message(message.chat.id, "Привет как мне страшно, Саша, позови Косолапуса")
    elif message.text.lower() == 'я твоя хозяйка':
        bot.send_voice(message.chat.id, 'AwACAgIAAxkBAAPNX-BHvH2OMbqM_o4xOK9EXhvd5UYAAqcLAAIaPAFLs4Rl43TciNAeBA')

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

@bot.message_handler(content_types=['voice'])
def sticker_id(message):
    print(message)

bot.polling()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
