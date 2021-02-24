def try_except(d,key):
	try:
		return d[key]
	except KeyError:
		return None

d = {'name': "Rockey"}
print(try_except(d, "city"))
#d["city"]
