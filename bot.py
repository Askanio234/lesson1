from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem
from answers import phrasedict, get_answer


def talk_to_me(bot, update):
    print('Пришло сообщение: {}'.format(update.message.text))
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
    else:
        result = 'Ошибка!'
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

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('killallhumans', kill_allhumans))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('showmeyourcat', show_me_your_cat))
    dp.add_handler(CommandHandler('planet',tell_constellation, pass_args = True))
    dp.add_handler(CommandHandler('wordcount', word_count, pass_args = True))
    dp.add_handler(CommandHandler('calc', calculator, pass_args = True))

    dp.add_handler(MessageHandler([Filters.text], talk_to_me))
    

    dp.add_error_handler(show_error)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
