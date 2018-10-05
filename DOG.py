class Dog:
	fur_color = "golden"
	eye_color = "blue"
	age = 3
	def __init__(self, name):
		self.name = name

my_dog = Dog("Freddy")
print(my_dog.name)