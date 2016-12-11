
def ask_user():
	while True:
		try:
			user_say = input('Как деала?  ')
			if user_say == 'Хорошо':
				break
		except KeyboardInterrupt:
			print('\nНу пока')
			break


def get_answer():
	while True:
		user_say = input('?')
		print('наверное...')
		if user_say == 'Пока':
			break


if __name__ == '__main__':
	ask_user()