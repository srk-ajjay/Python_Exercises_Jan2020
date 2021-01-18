#times = int(input("How many times do I have to tell you? :"))

#for var1 in range(times):
#	print("CLEAN YOUR ROOM !")
#	if var1 >= 3:
#		print("do you even listne anymore ? :")
##		break

times = int(input("How many times do I have to tell you? :"))

while times:
    print(f"{times}.CLEAN YOUR ROOM")
    times += 1
    if times >= 10:
        print("do you even listen to me anymore? :")
        break

