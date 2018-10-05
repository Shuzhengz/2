n = input("Input an interger between 0 and 100: ")
if pypt(n) == str:
	print("Whaaat?")
if int(n) > 0 and int(n) < 50:
	print("Your input is between 0 and 50!")
elif int(n) > 50 and int(n) < 100:
	print("Your input is between 50 and 100!")
elif int(n) < 0 or int(n) > 100:
	print("You didn't follow the instructions!")
else:
	print("Sorry, There's a bug")
print("See Ya!")