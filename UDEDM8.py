#UDEDM8 By Tom Zhang
#CC from Milo Kerr
from random import randint
y = int(input("Player Number: "))
p = int (input("Chance of dying (1 in something): "))
x = y
while y != 0:
	z = randint (1, p)
	if y == 1:
		break
	if z  ==  1:
		print ("UDEDM8")
		y = y - 1
	else:
		print ("UAIGHT")
print ("Player " + str(randint (1, x )) + " wins!")