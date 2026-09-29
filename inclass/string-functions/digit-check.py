user = input("Enter a number: ")

print(user.isdigit())
while user.isdigit() == False: 
    print("Not a valid number yet.")
    user = input("Enter a number: ")
print("Valid number now.")
user = int(user)
print(f"The number {user} squared is: {user**2}")

user = int(input("Enter a number: "))