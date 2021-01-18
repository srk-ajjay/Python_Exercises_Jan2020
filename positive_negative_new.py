from random import randint
x = randint(-100, 100)

while x == 0:  # make sure x isn't zero
    x = randint(-100, 100)
y = randint(-100, 100)
while y == 0:  # make sure y isn't zero
    y = randint(-100, 100)


if x<0 and y<0:
	print("Both Negative")
elif x>=0 and y >= 0:
	print("Both positive")
elif x<0 and y >=0:
	print("X is Negative & Y is positive")
elif y<0 and x >=0:
	print("X is Positive & Y is Negative")
else:
	print("Something is wrong")
