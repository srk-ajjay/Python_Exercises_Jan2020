print("...rock...")
print("...paper...")
print("...scissors...")

p1 = input("Enter Player 1 choice:")
p2 = input("Enter Player 2 choice:")

if p1 == "rock" and p2 == "scissors":
	print("Player 1 wins")
elif p1 == "paper" and p2 == "rock":
	print("Player 1 wins ")
elif p1 == "scissors" and p2 == "paper":
	print("Player 1 wins")
elif p1 == "scissors" and p2 == "rock":
	print("Player 2 Wins")
elif p1 == "rock" and p2 == "paper":
	print("Player 2 Wins")
elif p1 == "paper" and p2 == "scissors":
	print("Player 2 Wins")
elif p1 == p2:
	print("It's a tie!!!")
else:
	print("Something went wrong")
