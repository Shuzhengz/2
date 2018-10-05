a = ["milk", "pizza", "eggs", "cheese", "pizza", "lettuce"]
print(a)
print("Now displaying the reversed")
b = []
item = len(a)-1
while item >= 0:
	b.append(a[item])
	item = item - 1
print(b)