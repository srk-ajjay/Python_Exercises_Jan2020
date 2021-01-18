print("...rock...")
print("...paper...")
print("...scissors...")

p1 = input("Enter Player 1 choice:")
print("NO CHEATING !\n\n" * 20)
p2 = input("Enter Player 2 choice:")

if p1 == p2:
	print("It's a tie")
elif p1 == "rock":
	if p2 == "scissors":
		print("Player 1 wins")
	elif p2 == "paper":
		print("Player 2 Wins")

elif p1 == "paper":
        if p2 == "rock":
                print("Player 1 wins")
        elif p2 == "scissors":
                print("Player 2 Wins")

elif p1 == "scissors":
        if p2 == "rock":
                print("Player 2 wins")
        elif p2 == "paper":
                print("Player 1 Wins")
else:
	print("Something went wrong")
