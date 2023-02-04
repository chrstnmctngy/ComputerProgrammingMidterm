fullName = input("Submitted by: ")

print() #linebreak

print("Order Calculator")

print() #linebreak

shirtPrice = float(input("Shirt Price: ")) 
quantity = int(input ("Quantity: ")) 
product = shirtPrice*quantity

print() #linebreak

print("Order Summary: ")

print() #linebreak

centavos = format(shirtPrice, ".2f") #I use format to add decimal places since the outcome is 99.5 not 99.50.
print("You ordered " + str(quantity) + " shirts @ " + str(centavos) + " pesos per shirt." )
print("Your total order is " + str(product) + " pesos.")

print() #linebreak

cashTendered = float(input("Cash Tendered: "))
print("Change: " + str(cashTendered - product))

#https://codecollab.io/@jcvannymill/R12
