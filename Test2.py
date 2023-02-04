user_input = list(map(int, input("Enter 5 integer inputs: ").split()))

print("Output of All Input: ", user_input)

print("Maximum Input:", max(user_input))

print("Minimum Input: ", min(user_input))

def average(user_input):
    return sum(user_input) / len(user_input)

average1 = average(user_input)
print("Average: ", average1)

print("Sum: ", sum(user_input))

user_input.reverse()
print("Reverse: ", user_input)

def selectionSort(user_input):
    num = len(user_input)
    for i in range(num-1): 
        minValueIndex = i

        for j in range(i+1,num):
            if user_input[j] < user_input[minValueIndex] :
                minValueIndex = j

        if minValueIndex != i :
            temp = user_input[i]
            user_input[i] = user_input[minValueIndex]
            user_input[minValueIndex] = temp

    return user_input

selectionSort(user_input)
print("Selection Sort: ", user_input)
