if __name__ == '__main__':
	List = ['Вася', 'Маша','Петя', 'Валера', 'Саша', 'Даша']
	#while List:
		#person = List.pop()
		#if person == 'Валера':
			#print('Валера нашелся!')
			#break
	def find_person(name):
		while List:
			person = List.pop()
			if person == name:
				print('{} нашелся!'.format(name))

	find_person('Вася')
