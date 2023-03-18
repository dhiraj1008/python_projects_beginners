import random

print("Welcome To Password Generator")
chars="!@#$%^&*()AQWSEDRFTGYHUJIKOLPZXCBVNMasdfghjklmnbvcxzqwertyuiop"
count=int(input("Amount of  passwords to generate?"))
length=int(input("length of the passwords ?"))
print("Here are your passwords :")
for i in  range(count):
    password=""
    for j in range(length):
        password+=random.choice(chars)
    print(password)
