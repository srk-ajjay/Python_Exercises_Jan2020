playlist = {
	'title': "Patagonia bus",
	'author': "Brodha V",
	'songs': [
		{'title': 'song1', 'artist': ['paul'], 'duration': 2.5},
		{'title': 'song2', 'artist': ['back','simon'], 'duration': 5.25},
		{'title': 'song3', 'artist': ['rihanna'], 'duration': 2.1},
	]
}

total_length = 0
for var in playlist['songs']:
	total_length = total_length + var['duration']

print(total_length)
