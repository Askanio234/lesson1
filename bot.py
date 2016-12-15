from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem
from answers import phrasedict, get_answer
from cities import load_city_list


def talk_to_me(bot, update):
    print('Пришло сообщение: {}'.format(update.message.text))
    global isPlayingCities
    global CITIES
    if isPlayingCities:
        input = update.message.text.lower()
        if input not in CITIES:
            bot.sendMessage(update.message.chat_id, text="{} либо был уже, либо нет такого города".format(input))
        else:
            reply = choose_city(bot, update, input, CITIES)
            bot.sendMessage(update.message.chat_id, text="{}, Ваш ход".format(reply))
    else:
        if 'сколько будет' in update.message.text.lower():
            calc_verbally(bot, update)
        elif 'полнолуние' in update.message.text.lower():
            when_next_fullmoon(bot, update)
        else:
            bot.sendMessage(update.message.chat_id, get_answer(update.message.text, phrasedict))


def show_error(bot, update, error):
    print('Update "{}" caused error "{}"'.format(update, error))


def help(bot, update):
    print("Вызван /помощь")
    bot.sendMessage(update.message.chat_id, text='/start \n/killallhumans \n/showmeyourcat \n/planet planetname(eng) \n/wordcount "word"')
    print(update.message)

isPlayingCities = False
CITIES = []
def play_cities(bot, update, args):
    print("Вызван /города")
    global isPlayingCities
    global CITIES
    isPlayingCities = True
    CITIES = load_city_list()
    reply = choose_city(bot, update, args[0],CITIES)
    bot.sendMessage(update.message.chat_id, text ="{}, Ваш ход".format(reply))

# На основе выбора игрока выбирает новый город, мутирует лист. Input = "str"
def choose_city(bot, update, input, list_of_cites):
    for city in list_of_cites:
        if input == city:
            list_of_cites.remove(city)
    if input[-1] in 'ыьй':
        last_letter = input[-2]
    else:
        last_letter = input[-1]
    for city in list_of_cites:
        if city[0] == last_letter:
            list_of_cites.remove(city)
            return city


def stop_play_cities(bot, update):
    print('Вызван /cancel')
    global isPlayingCities
    global CITIES
    isPlayingCities = False
    CITIES = []
    bot.sendMessage(update.message.chat_id, text='Все прекращаем!')

def greet_user(bot,update):
    print("Вызван /старт")
    bot.sendMessage(update.message.chat_id, text='Давай общаться! Не знаешь что написать? попробуй /help')
    print(update.message)


def show_me_your_cat(bot, update):
    print('Вызван /showmeyourcat')
    bot.sendPhoto(update.message.chat_id, photo='https://pp.vk.me/c303300/v303300996/43f1/kxMJre_gSrY.jpg')
    print(update.message)


def kill_allhumans(bot, update):
    print("Вызван /убитьвсехчеловеков")
    bot.sendMessage(update.message.chat_id, text='Убить всех человеков через 3...2...1..')
    print(update.message)


def when_next_fullmoon(bot, update):
    input = update.message.text.split(" ")
    date = input[4]
    answer = ephem.next_full_moon(date)
    bot.sendMessage(update.message.chat_id, text = str(answer))


def tell_constellation(bot, update, args):
    print('Вызван /planet')
    input = args[0].capitalize()
    if input == "Mars":
        planet = ephem.Mars()
    if input == "Neptune":
        planet = ephem.Neptune()
    if input == "Venus":
        planet = ephem.Venus()
    if input == "Mercury":
        planet = ephem.Mercury()
    if input == "Jupiter":
        planet = ephem.Jupiter()
    if input == "Saturn":
        planet = ephem.Saturn()
    if input == "Uranus":
        planet = ephem.Uranus()

    planet.compute()
    print(planet)
    try:
        string = ephem.constellation(planet)[1]
        bot.sendMessage(update.message.chat_id, text = string)
    except:
        bot.sendMessage(update.message.chat_id, text = 'Эй, это не планета!')

def word_count(bot, update, args):
    print('Вызван /wordcount')
    count = 0
    for item in args:
        if item != '"':
            count +=1
    
    bot.sendMessage(update.message.chat_id, text = '{} слова.'.format(count))


def calculator(bot, update, args):
    print('Вызван /calculator')
    if '+' in args[0]:
        input = args[0].split('+')
        answer = int(input[0]) + int(input[1])
    if '-' in args[0]:
        input = args[0].split('-')
        answer = int(input[0]) - int(input[1])
    if '*' in args[0]:
        input = args[0].split('*')
        answer = int(input[0]) * int(input[1])
    if '/' in args[0]:
        input = args[0].split('/')
        try:
            answer = int(input[0]) / int(input[1])
        except ZeroDivisionError:
            answer = 'Деление на ноль не определено!'
    if ' ' in args[0]:
        answer = 'Пробелы недопустимы!'
    bot.sendMessage(update.message.chat_id, text = str(answer))


def calculate(input, a, b):
    if input == 'плюс':
        result = a + b
    if input == 'минус':
        result = a - b
    if input == 'умножить':
        result = a * b
    if input == 'разделить' and b != 0:
        result = a/b
    return result


def calc_verbally(bot, update):
    numbers = {
    'ноль':0, 'один':1, 'два':2, 'три':3,'четыре':4, 'пять':5, 
    'шесть':6, 'семь': 7, 'восемь': 8, 'девять':9, 'десять':6,
    }
    input = update.message.text.split(' ')
    a = numbers[input[2]]
    if 'на' in update.message.text:
        b = numbers[input[5]]
    else:
        b = numbers[input[4]]
    answer = str(calculate(input[3],a,b))
    bot.sendMessage(update.message.chat_id, text = answer)

def main():
    updater = Updater("326458218:AAEKVLRflUisJUNY5JijTnTObHeacdPBQsQ")
    isPlayingCities = False
    CITIES = []
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('killallhumans', kill_allhumans))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('showmeyourcat', show_me_your_cat))
    dp.add_handler(CommandHandler('planet',tell_constellation, pass_args = True))
    dp.add_handler(CommandHandler('wordcount', word_count, pass_args = True))
    dp.add_handler(CommandHandler('calc', calculator, pass_args = True))
    dp.add_handler(CommandHandler('goroda', play_cities, pass_args = True))
    dp.add_handler(CommandHandler('cancel', stop_play_cities))

    dp.add_handler(MessageHandler([Filters.text], talk_to_me))
    
    
    dp.add_error_handler(show_error)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
