user_input = list(map(int, input("Enter 10 inputs: ").split()))

def bubbleSort(user_input):
    num = len(user_input)
    for i in range(num-1):
        for j in range(0, num-i-1):
            if user_input[j] > user_input[j + 1] :
                user_input[j], user_input[j + 1] = user_input[j + 1], user_input[j]

bubbleSort(user_input)
print("Bubble Sort: ", user_input)

def selectionSort(user_input):
    num = len(user_input)
    for i in range(num-1): 
        minValueIndex = i
        for j in range(i+1, num):
            if user_input[j] < user_input[minValueIndex] :
                minValueIndex = j
        if minValueIndex != i :
            temp = user_input[i]
            user_input[i] = user_input[minValueIndex]
            user_input[minValueIndex] = temp
    return user_input

selectionSort(user_input)
print("Selection Sort: ", user_input)

def insertionSort(user_input):
    for i in range(1, len(user_input)):
        key = user_input[i]
        j = i-1
        while j >=0 and key < user_input[j] :
                user_input[j+1] = user_input[j]
                j -= 1
        user_input[j+1] = key
  
insertionSort(user_input)
print("Insertion Sort: ", user_input)

print("Minimum of 10 inputs: ", min(user_input))
print("Maximum of 10 inputs: ", max(user_input))
print("Sum of 10 inputs: ", sum(user_input))
