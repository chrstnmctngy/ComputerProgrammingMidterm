user_input = list(map(int, input("Enter 5 integer inputs: ").split()))

for num in user_input:
    print("Output of All Input: ", user_input)
    break

max_input = None
 
for num in user_input:
    if (max_input is None or num > max_input):
        max_input = num

print("Maximum Input: ", max_input)

min_input = None

for num in user_input:
    if (min_input is None or num < min_input):
        min_input = num

print("Minimum Input: ", min_input)

def input_average(user_input):
    return sum(user_input) / len(user_input)

average1 = input_average(user_input)
print("Average of All Inputs: ", average1)

sum = 0
for num in user_input:
      sum = sum + num

print("Sum of All Inputs: ", sum)

def reverse_input(user_input):
    for num in range(len(user_input)-1, -1, -1):
        yield user_input[num]

print("Reverse of All Inputs : ", list(reverse_input(user_input)))

def bubbleSort(user_input):
    num = len(user_input)
    for i in range(num-1):
        for j in range(0, num-i-1):
            if user_input[j] > user_input[j + 1] :
                user_input[j], user_input[j + 1] = user_input[j + 1], user_input[j]

bubbleSort(user_input)
print("Sorted Inputs: ", user_input)

for i in user_input:
    if (i==5):
        print("Yes")
        break
    else:
        print("No")
        break

    [1, 2, 3, 4, 5]

user_input.reverse


