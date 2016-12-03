if __name__ == '__main__':
	phrasedict = {"привет":"И тебе привет!", "как дела":"Лучше всех", "пока":"Увидимся"}
	def get_answer(key, dict):
		print(dict.get(key.lower()))
	user_choice = input("Введите фразу: ")
	get_answer(user_choice,phrasedict)