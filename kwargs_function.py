def fav_color(**pet):
	for animal,color in pet.items():
		print(f"{animal} color is {color}")

fav_color(pigeon="white", dog="brownie", cat="silver")
