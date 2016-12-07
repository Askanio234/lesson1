if __name__ == '__main__':
	grades = [{'school_class': '4a', 'scores': [4,4]}, {'school_class': '4b', 'scores':[5,5]}, 
	{'school_class': '4c', 'scores':[3,3]}]
	def mean_by_school(school):
		mean = 0
		for school_class in school:
			temp = school_class.get('scores')
			mean += sum(temp)/len(temp)
		return mean/len(grades)

	def mean_by_class(school):
		answer = ''
		for school_class in school:
			temp = school_class.get('scores')
			answer += school_class.get('school_class') + ' ' + str(sum(temp)/len(temp)) + ';'
		return answer

	print(mean_by_school(grades))
	print(mean_by_class(grades))

