from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def talk_to_me(bot, update):
    print('Пришло сообщение: {}'.format(update.message.text))
    bot.sendMessage(update.message.chat_id, update.message.text)

def show_error(bot, update, error):
    print('Update "{}" caused error "{}"'.format(update, error))

def greet_user(bot,update):
	print("Вызван /старт")
	bot.sendMessage(update.message.chat_id, text='Давай общаться!')
	print(update.message)


def main():
	updater = Updater("326458218:AAEKVLRflUisJUNY5JijTnTObHeacdPBQsQ")

	dp = updater.dispatcher
	dp.add_handler(CommandHandler("start", greet_user))

	dp.add_handler(MessageHandler([Filters.text], talk_to_me))

	dp.add_error_handler(show_error)

	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
    main()