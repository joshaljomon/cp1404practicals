PASSWORD_LENGTH = 10

password = input("Enter a password: ")
while len(password) < PASSWORD_LENGTH:
    print("Invalid password")
    password = input("Enter a password: ")
for  i in range(len(password) + 1):
    print('*', end="")