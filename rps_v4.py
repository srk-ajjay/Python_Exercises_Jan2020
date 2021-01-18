from random import randint

rand_num = randint(0,2)

if rand_num == 0:
	computer = "rock"
elif rand_num == 1:
	computer = "paper"
else:
	computer = "scissors"

p1 = input("Enter your choice:").lower()
#computer = input("Enter Player 2 choice:")

if p1 == computer:
	print("It's a tie")
elif p1 == "rock":
	if computer == "scissors":
		print("Player 1 wins")
	elif computer == "paper":
		print("Computer Wins")

elif p1 == "paper":
        if computer == "rock":
                print("Player 1 wins")
        elif computer == "scissors":
                print("Computer Wins")

elif p1 == "scissors":
        if computer == "rock":
                print("Computer wins")
        elif computer == "paper":
                print("Player 1 Wins")
else:
	print("Something went wrong")
