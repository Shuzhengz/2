piece = "false"
score = 0
class Ro:
	def __init__(self, pos, armp):
		self.armp = armp
		self.pos = pos
	def move(self, dist):
		self.pos += dist
	def claw(self, dist):
		self.armp += dist
Rob = Ro(0, 0)
print('''To move, type in move
To lower arm, type la
to raise arm, type ra
to tight claw, type tc
to loose claw, type lc
To stop, type Stop''')
x = 1
while x == 1:
	ins = input("Instructiuon: ")
	if ins == "move":
		y = int(input("How mutch: "))
		Rob.move(y)
		print(Rob.pos)
		print(Rob.armp)
		print(piece)
	elif ins == "la":
		if Rob.armp > 0:
			z = int(input("How mutch: "))
			Rob.claw(-z)
			print(Rob.pos)
			print(Rob.armp)
			print(piece)
	elif ins == "ra":
		if Rob.armp < 11:
			z = int(input("How mutch: "))
			Rob.claw(z)
			print(Rob.pos)
			print(Rob.armp)
			print(piece)
	elif ins == "tc":
		if Rob.armp == 0 and Rob.pos == 3 and piece == "false":
			piece = "true"
			print(Rob.pos)
			print(Rob.armp)
			print(piece)
		else:
			print("Error: Your arm needs to be on the ground!")
	elif ins == "lc":
		piece = "false"
		print(Rob.pos)
		print(Rob.armp)
		print(piece)
	elif ins == "Stop":
		x = x - 1
		print(Rob.pos)
		print(Rob.armp)
		print(piece)
	if Rob.pos == 7 and Rob.armp == 10 and piece == "true":
		score = score + 5
		piece = "false"
	print("Score: " + str(score))
print(Rob.pos)
print(Rob.armp)
print(piece)
print("Final Score: " + str(score))