phrasedict = {"привет":"И тебе привет!", "как дела?":"Лучше всех", "пока":"Увидимся"}
def get_answer(key, dict):
	if key.lower() in dict:
		return dict.get(key.lower())
	else:
		return "Я не понял, попробуй другую фразу..."

if __name__ == '__main__':
	
	user_choice = input("Введите фразу: ")
	get_answer(user_choice,phrasedict)