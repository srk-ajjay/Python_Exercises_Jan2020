instructor = {
	"name": "Colt",
	"num_subject": "My Wish",
	"favourite language": "Python",
}
answer = {k.upper():v.upper() for k,v in instructor.items()}
print(answer)
