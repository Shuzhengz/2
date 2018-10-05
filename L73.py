passwords = {"1" : 10, "2" : 20, "3" : 30, "4" : 40, "5" : 50, "6" : 60, "7" : 70, "8" : 80, "9" : 90, "10" : 100}
bom = 1
print("to add an account, please enter  'your password:value' in the source code")
print("to remove value, enter 'pop'")
print("to exit, press Ctrl and C together")
while bom == 1:
	x = input("enter your password: ")
	if x in passwords:
		print("$" + str(passwords[x]))
	else:
		print("Wrong Password")
	y = input("Enter your command: ")
	if y == "pop":
		y = input("Which password would you wnat to remove: ")
		passwords.pop(y)
		print("removed")