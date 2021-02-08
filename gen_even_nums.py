def generate_evens():
	result = []
	for x in range(1,50):
		if x % 2 == 0:
			result.append(x)
	return result


print(generate_evens())
