if __name__ == '__main__':
	user_age = int(input('Введите Ваш возраст '))
	if user_age < 7:
		print('Вы должны быть в детском саду!')
	elif 7 <= user_age <= 17:
		print('Вы должны быть в школе!')
	elif 18 <= user_age <= 23:
		print('Вы должны быть в институте!')
	elif 24 <= user_age:
		print('Вы должны быть на работе!')