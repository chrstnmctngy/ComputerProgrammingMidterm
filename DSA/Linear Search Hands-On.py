x = []

z = int(input("Enter a number: "))
x.append(z)

while z != -1:
	z = int(input("Enter a number: "))
	x.append(z)

def linearC(x, c):
	for j in range(0, len(x)):
		if (x[j] == c):
			x = print(str(c) + " found at index " + str(j))
			return x
	else:
		print("The value index is not found")

c = int(input("What number would you like to c? "))
linearC(x, c)