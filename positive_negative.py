from random import randint

x = randint(-100, 100)
print(f" {x}")
while x != 0:  # make sure x isn't zero
    x = randint(-100, 100)
    print(f"{x}")
    if x > 0:
        print(f" x = {x} is Positive Number")
    elif x < 0:
        print(f" x = {x} is Negetive Number")
y = randint(-100, 100)
while y != 0:  # make sure y isn't zero
    y = randint(-100, 100)
    print(f"{y}")
    if y > 0:
        print(f" y = {y} is Positive Number")
    elif y < 0:
        print(f" y = {y} is Negetive Number")

