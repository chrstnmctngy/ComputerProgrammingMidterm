userInput = int(input("How many inputs? "))

list = []

for i in range(userInput):
    list.append(input("Enter Input: "))

print("Unsorted: ", list)

def bubbleSort(list):
    for i in range(len(list)):
        for j in range(0, len(list)-i-1):
            if list[j] > list[j + 1] :
                list[j], list[j + 1] = list[j + 1], list[j]

bubbleSort(list)
print("Sorted: ", list)