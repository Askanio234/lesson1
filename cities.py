
cities_filename = 'cities.txt'

def load_city_list():
	print('Загрузка списка городов')
	city_list = []
	with open(cities_filename, 'r') as f:
		for line in f:
			city_list.append(line.rstrip().lower())
	return city_list


if __name__ == '__main__':
	x = load_city_list()
	print(x[0])
	print(x[100])