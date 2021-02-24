#def sum_of_all(num1,num2,num3,num4,num5):
#	return num1+num2+num3+num4+num5

#print(sum_of_all(3,6,8,5,2))

def sum_of_all(*nums):
	total = 0
	for num in nums:
		total += num
	return total

print(sum_of_all(3,6,8,5,2))
print(sum_of_all(5,2))
