#Write a program to convert kilometers to miles, you ran
#/// miles = kms/1.60934

#kms = 10
kms = input("How many kilometers did you cycle today?: ")
#kms = input()
miles = float(kms)/1.60934 # convert from string to float and then divide
miles = round(miles, 2) # round the result to 2 after decimal
print(f"Your {kms} km ride was {miles}mi")

