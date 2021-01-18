#Below 2 no ticket
#Above 2 & Below 8 half/child ticket
#above 8 full ticket

age = input("Enter age: ")
if age:
	age = int(age)
	if age <= 2:
		print("No ticket")
	elif age > 2 and age <=8:
		print("Child ticket")
	else:
		print("Full ticket")
else:
	print("You forgot to enter age")
