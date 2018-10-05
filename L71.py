word = ["ha", "what", "shoot", "why", "rip", "how", "apple", "python", "coding", "programming"]
x = input("Your word(no caps): ")
if x in word:s
	print("This word already exist")
else:
	word.append(x)
print(word)