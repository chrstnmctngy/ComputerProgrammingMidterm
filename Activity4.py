print("Submitted By: Macatangay, Christian R. (R12)")

print()

username = ["user1", "user2", "user3", "user4",]
password = ["user1", "user2", "user3", "user4"]

currUsername = input ("Username: ") 
currPassword = input ("Password : ")

for index in range(len(username)):
    if username[index] == currUsername and password[index] == currPassword: 
      print("Welcome, " + username[index])
      break
else:
    print("Account not found.") 