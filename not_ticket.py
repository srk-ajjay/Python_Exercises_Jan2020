#take age as input
#age 2-8 = 2 dollars ticket
# age above 65  = 5 dollar ticket
## all othere 10 dollars i.e. in between 8 * 65


age = input("Enter you age: ")
age = int(age)

#if age >= 2 and age <= 8:
#	print("2 dollars ticket")
#elif age >= 65:
#	print(" 5 dollars ticket")
#else:
###	print("10 dollar ticket")

if not ((age >= 2 and age <= 8) or age > 65)
	print("10 dollar ticket")
else
	print("You are a child or senior")
