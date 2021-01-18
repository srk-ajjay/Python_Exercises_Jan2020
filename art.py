#for x in range(5):
#	for num in range(1, 9):
#		print("\U0001f600" * num)

times = 1 
pyramid = 1
while pyramid < 5:
	while times < 9:
		print("\U0001f600" * times)
		times += 1
	pyramid += 1
	times = 1 
