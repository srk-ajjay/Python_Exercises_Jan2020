from random import choice
food = choice(['apple','grape', 'bacon', 'steak', 'worm'])

print(food)
if food == "apple" or food == "grape":
    print("Its a Fruit")
elif food == "bacon" or food == "steak":
    print("Its a Meat")
else:
    print("Yuck")

