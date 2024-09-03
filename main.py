import random

symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

password_length = int(input("Enter password length: "))

password = ""

for i in range(password_length):
    password = password + random.choice(symbols)

print("Your password is : " + password)
