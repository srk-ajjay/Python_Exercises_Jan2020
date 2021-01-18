#ask for age
#18-21 wristband
#21+ drink, normal entry
# too young, sorry
age = input("What is your age?: ")
#age = int(age)
if age:
    age = int(age)
    if age == 18 and age < 21:
        print("Wear a Wristband")
    elif age >= 21:
        print("Normal entry with drinks")
    else:
        print("Sorry you are too young")
else:
    print("You have not mentioned your age")

