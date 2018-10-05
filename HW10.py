class robot:
	def __init__(self, pos, armp, cube, score):
		self.pos = pos
		self.armp = armp
		self.cube = cube
		self.score = score
	def iterative_robot(self, dist, level, pick):
		self.pos  += dist
		self.armp += level
		if self.pos == 3 and pick == True:
			self.cube = True
			print('picked', self.cube)
		else:
			self.cube = self.cube
rob1 = robot(0,0,False,0)
for i in range(0,10):
	pos, level, pick = int(input("move:  ")), int(input("height:  ")), bool(input("pick:  "))
	rob1.iterative_robot(pos, level, pick)
	if rob1.pos == 7 and rob1.armp == 10 and rob1.cube == True :
		rob1.score += 5
		rob1.cube = False
	print(rob1.score, rob1.pos, rob1.armp, rob1.cube)