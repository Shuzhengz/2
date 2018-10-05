def L92(a, b):
	if a % b == 0:
		print("true")
		print("The number is divisible")
	else:
		print("false")
		print("The number is not divisible")
x = int(input("first number: "))
y = int(input("second number: "))
L92(x, y)