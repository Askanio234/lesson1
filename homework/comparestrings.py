
def compare(string_a, string_b):
	if string_a == string_b:
		return 1
	else:
		if string_a > string_b:
			return 2
		elif string_b == 'learn':
			return 3

if __name__ == '__main__':
	print(compare('asda','asda'))
	print(compare('asdas', 'asda'))
	print(compare('asdas', 'learn'))