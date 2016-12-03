if __name__ == '__main__':
	user_info = {"first_name":"Artem", "last_name":""}
	print(user_info.get("first_name"))
	user_info["last_name"] = input("Введите фамилию: ")
	print(user_info)