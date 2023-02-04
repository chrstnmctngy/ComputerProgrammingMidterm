lst = []

num = 3

for n in range(num):
    numbers = int(input("Enter number: "))
    lst.append(numbers)
  
search = int(input("What number would you like to search? "))

i = 0
flag = False

while i < len(lst):
	if lst[i] == search:
		flag = True
		break
	i = i + 1

if flag == 1:
	print(str(search) + " found at index " + str(i) + ".")
else:
	print(str(search) + " not found.")

print()

lst = []

num = 5

for n in range(num):
    numbers = int(input("Enter number: "))
    lst.append(numbers)
  
search = int(input("What number would you like to search? "))

i = 0
flag = False

while i < len(lst):
	if lst[i] == search:
		flag = True
		break
	i = i + 1

if flag == 1:
	print(str(search) + " found at index " + str(i) + ".")
else:
	print(str(search) + " not found.")