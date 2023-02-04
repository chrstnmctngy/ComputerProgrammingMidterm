print("Submitted By: Macatangay, Christian R. (R12)")

print() #linebreak

print("Order Calculator")

print() #linebreak

shirtPrice = float(input("Shirt Price: ")) 
quantity = int(input ("Quantity: ")) 
product = float(shirtPrice*quantity)
discounted = float(product*0.20)

print() #linebreak

print("Order Summary: ")
print("Item: Shirt")
print("Quantity: " + str(quantity) + " pcs.")
print("Total " + str(product) + " pesos")

print() #linebreak

membership = input("Has membership card? (yes/no) : ")

if membership == "yes":
    print("Order Total: " + str(product))
    print("Discount: " + str(discounted))
    print("Total Among Due: " + str(product-discounted))
    cashTendered = float(input("Cash Tendered: "))
    print("Change: " + str(cashTendered-(product-discounted)))

else:
    print("Order Total: " + str(product))
    cashTendered = float(input("Cash Tendered: "))
    print("Change: " + str(cashTendered-product))



