#Lesson 1
def ptage():
	age = "14"
	print("Tom Zhang")
	print("Age: " + age)
	print(int(age) * 12)
ptage()

#Lesson 2
def L2():
	name = input("Your name: ")
	x = input("How many pizzas you want? ")
	y = input("How many pieces of pepperoni do you want?  ")
	z = input("How many olives do you want? ")
	print(name + " wants " + x + " pieces of the stupid pizzas, " + y + " pieces of pepperoni(s), and " + z + " gigantic olives.")
	print("ThankYouComeAgain")
	name2 = input("Your name: ")
	x2 = input("How many pizzas you want? ")
	y2 = input("How many pieces of pepperoni do you want?  ")
	z2 = input("How many olives do you want? ")
	print(name2 + " wants " + x2 + " pieces of the stupid pizzas, " + y2 + " pieces of pepperoni(s), and " + z2 + " gigantic olives.")
	print("ThankYouComeAgain")
	name3 = input("Your name: ")
	x3 = input("How many pizzas you want? ")
	y3 = input("How many pieces of pepperoni do you want?  ")
	z3 = input("How many olives do you want? ")
	print(name3 + " wants " + x3 + " pieces of the stupid pizzas, " + y3 + " pieces of pepperoni(s), and " + z3 + " gigantic olives.")
	print("ThankYouComeAgain")
	x = int(x)
	x2 = int(x2)
	x3 = int(x3)
	y = int(y)
	y2 = int(y2)
	y3 = int(y3)
	z = int(z)
	z2 = int(z2)
	z3 = int(z3)
	print('''
	Average:''')
	print("Pizzas: " + str((float(x) + float(x2) + float(x3))/3))
	print("Pepperonis: " + str((float(y) + float(y2) + float(y3))/3))
	print("Olives: " +str((float(z) + float(z2) + float(z3))/3))

L2()
#Lesson 4
#Done with shell, didn't have a file

#Lesson 5
def L5():
	n = input("Input an interger between 0 and 100: ")
	if int(n) > 0 and int(n) < 50:
		print("Your input is between 0 and 50!")
	elif int(n) > 50 and int(n) < 100:
		print("Your input is between 50 and 100!")
	elif int(n) < 0 or int(n) > 100:
		print("You didn't follow the instructions!")
	else:
		print("Sorry, There's a bug")
	print("See Ya!")
L5()

#Lesson 5 (Homework)
def L5_1():
	a = int(input("What is your age? "))
	if a >= 14:
		print("You could join the Robotics Team.")
	if a >= 16:
		print("You could drive and get a job.")
	if a >= 18:
		print("You can attend to college")
	if a == 21:
		print("Congrats! You are now an adult (which totally sucks).")
	if a > 21:
		print("You are an adult.")
	if a >= 35:
		print("You could become the President.")
	if a < 14:
		print("Sorry, you couldn't do anything...")
L5_1()

#Lesson 6
def L6():
	patients = [[70, 1.8], [80, 1.9], [150, 1.7]]
	def calculate_bmi(weight, height):
		return weight / (height ** 2)
	for patient in patients:
		weight, height = patients[0]
		bmi = calculate_bmi(height, weight)
	print("Patient's BMI is:" + str(bmi))
L6()

#Lesson 7(1)
def L71():
	word = ["ha", "what", "shoot", "why", "rip", "how", "apple", "python", "coding", "programming"]
	x = input("Your word(no caps): ")
	if x in word:
		print("This word already exist")
	else:
		word.append(x)
	print(word)
L71()

#Lesson 7(2)
def L72():
	data = []
	data.append(input("What is your name: "))
	data.append(input("What is your favoriate colour: "))
	data.append(input("How many pet(s) do you have: "))
	print(data[0] + "'s favoriate colour is " + data[1] + ". He/She has " + data[2] + " pets.")
L72()

#Lesson 7(3)
def L73():
	passwords = {"1" : 10, "2" : 20, "3" : 30, "4" : 40, "5" : 50, "6" : 60, "7" : 70, "8" : 80, "9" : 90, "10" : 100}
	bom = 1
	print("to add an account, please enter  'your password:value' in the source code")
	print("to remove value, enter 'pop'")
	print("to exit, type in exit")
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
		if y == "exit":
			bom = bom - 1
L73()

#Lesson 8(1)
def L81():
	x = []
	y = input("")
	z = 1
	while z == 1:
		if y == "Stop" or y == "stop":
			z = z - 1
		else:
		 	x.append(y)
	print(x)
L81()

#Lesson 8(2)
def L82():
	a = ["milk", "pizza", "eggs", "cheese", "pizza", "lettuce"]
	print(a)
	print("Now displaying the reversed")
	b = []
	item = len(a)-1
	while item >= 0:
		b.append(a[item])
		item = item - 1
	print(b)
L82()
print("DONE")