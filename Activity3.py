print("Submitted By: Macatangay, Christian R. (R12)")

print() #linebreak

lives = 3

while lives <= 3: 
    print("Lives: " + str(lives)) 
    sum = int(input("100 + 50 = ")) 
    if sum == 150:
        print("You won!")
        break

    else:
        lives = lives - 1
        if lives <= 0:
            print() #linebreak
            print("Lives: " +str(lives)) 
            print("You lose.") 
            break
    print() #linebreak