import random
import string

length = int(input("Enter password length: "))
if length < 8:
    print("Password length should be at least 8 for complexity.")
    exit()

chars = string.ascii_letters + string.digits
password = ""

for i in range(length):
    password += random.choice(chars)

print("Generated Password:", password)