#UDEDM8 By Tom Zhang
#CC from Milo Kerr
from random import randint
y = int(input("Player Number: "))
while y == 0:
    print("There must be at least one player!")
    y = int(input("Enter again: "))
p = int(input("Chance of dying (1 in something): "))
while p == 0:
    print("Chance of dying cannot be zero!")
    p = int(input("Enter again: "))
x = y
while y != 0:
	z = randint (1, p)
	if y == 1:
		break
	if z  ==  1:
		print ("UDEDM8 (" + str(randint(1 , x)) + ")")
		y = y - 1
	else:
		print ("UAIGHT")
print ("Player " + str(randint(1 , x )) + " wins!")
