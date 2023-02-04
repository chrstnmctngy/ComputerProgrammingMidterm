print("Submitted by: Christian R. Macatangay (1R12)")

print()

lst = []

user_input = int(input("Enter a number: "))
lst.append(user_input)

while user_input != -1:
	user_input = int(input("Enter a number: "))
	lst.append(user_input)

def bubbleSort(lst):  
    for i in range(0, len(lst)-1):  
        for j in range(len(lst)-1):  
            if(lst[j] > lst[j + 1]):  
                temp = lst[j]  
                lst[j] = lst[j + 1]  
                lst[j + 1] = temp  
    return lst

lst.pop()
bubblesort = bubbleSort(lst)
print("Sorted numbers: " + str(bubblesort))

def binarySearch(lst, key):
    low = 0
    high = len(lst)
    while low < high:
        mid = (low + high)//2
        if lst[mid] > key:
            high = mid
        elif lst[mid] < key:
            low = mid + 1
        else:
            return mid
    return -1
 
key = int(input("What number would you like to search? "))
result = binarySearch(lst, key)	
if result < 0:
    print("The value index is not found")
else:
    print(str(key) + " found at index " + str(result))
