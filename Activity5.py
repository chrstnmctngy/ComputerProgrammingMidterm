print("Activity 5")
print("Submitted by: Christian R. Macatangay │ R12")

print()

num_1 = int(input("Input first number: "))
num_2 = int(input("Input second number: "))

print()

print("Choose Operation:")
print("[1] Addition")
print("[2] Subtraction")
print("[3] Multiplication")
print("[4] Division")

print()

num_3 = int(input("Operation: "))

print()

def add(num_1, num_2):
    sum = num_1 + num_2
    return sum

def sub(num_1, num_2):
    dif = num_1 - num_2
    return dif

def mul(num_1, num_2):
    pro = num_1 * num_2
    return pro

def div(num_1, num_2):
    qou = num_1 / num_2
    return qou

if num_3 == 1:
    total_0 = add(num_1, num_2)
    print("Sum: " +  str(num_1) + " + " + str(num_2) + " = " + str(total_0))

elif num_3 == 2:
    total_1 = sub(num_1, num_2)
    print("Difference: " +  str(num_1) + " - " + str(num_2) + " = " + str(total_1))

elif num_3 == 3:
    total_2 = mul(num_1, num_2)
    print("Product: " +  str(num_1) + " * " + str(num_2) + " = " + str(total_2))

elif num_3 == 4:

    total_3 = div(num_1, num_2)
    print("Quotient: " +  str(num_1) + " / " + str(num_2) + " = " + str(total_3))

else:
    print("Invalid operation")

    