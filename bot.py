from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem
from answers import phrasedict, get_answer


def talk_to_me(bot, update):
    print('Пришло сообщение: {}'.format(update.message.text))
    bot.sendMessage(update.message.chat_id, get_answer(update.message.text, phrasedict))

def show_error(bot, update, error):
    print('Update "{}" caused error "{}"'.format(update, error))

def help(bot, update):
    print("Вызван /помощь")
    bot.sendMessage(update.message.chat_id, text='/start \n/killallhumans \n/showmeyourcat \n/planet planetname(eng)')
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
    if input == "Earth":
        planet = ephem.Earth()
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


    
def main():
    updater = Updater("326458218:AAEKVLRflUisJUNY5JijTnTObHeacdPBQsQ")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('killallhumans', kill_allhumans))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('showmeyourcat', show_me_your_cat))
    dp.add_handler(CommandHandler('planet',tell_constellation, pass_args = True))

    dp.add_handler(MessageHandler([Filters.text], talk_to_me))

    dp.add_error_handler(show_error)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()