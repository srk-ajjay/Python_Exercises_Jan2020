import random

random_number = random.randint(1,10)  # numbers 1 - 10

user = None

while True:
    user = int(input("Enter number between 1 to 10: "))
    if user > random_number:
        print(random_number)
        print("your number is too high ")
    elif user < random_number:
        print(random_number)
        print("your number is too low ")
    else:
        print("YOU WON !!!!")
        play_again = input("Do you want to play again?(y/n): ")
        if play_again == "y":
                random_number = random.randint(1,10) 
                user = None
        else:
                print("Thank you for playing")
                break

