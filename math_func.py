def add(a,b):
	return a+b

def math(a,b, c=add):
	return c(a,b)

def subtact(a,b):
	return a-b


print(math(2,2)) #4
print(math(2,2, subtact))
