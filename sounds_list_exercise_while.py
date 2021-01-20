#List Interation:
#I've given you a list called sounds. It looks like this:
sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
##=> Write code that loops ove the list and adds all the strings together to form one large combined
#string(don't) add any spaces between them)
#=> The combined string should be in all UPPERCASE as well

sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

result = 0
adding = ''

while result < len(sounds):
	adding += sounds[result]
	result += 1

adding=adding.upper()
print(adding)
