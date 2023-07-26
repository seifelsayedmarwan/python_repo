import random

#A simple code to create a strong random password in case you need it.
#  You just have to specify the length of the password and it will generate it

def create_password(length):
    password = ""
    char = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz@#$&"
    for _ in range(length):
        password += random.choice(char)
    return password

while True:
    pass_length = int(input("Enter password length:\t"))
    print(create_password(pass_length))
    go_back = input("Type back to back first or press enter to exit:\t")
    if go_back.lower() == "back":continue
    else:break