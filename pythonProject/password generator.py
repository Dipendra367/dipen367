#randomly generate the password

import random

word= "qwertyuiopasdfghjklzxcvbnmQWERTYUIOASDFGHJKLZXCVBNM123456789@#$%&*_-+/\!"
while True:
    length=int(input("Enter the length of the password you want to generate : "))

    pat="".join(random.sample(word,length))
    print()
    print("Your password is  : ", pat)

    print()

    d=input("Do you wnt to generate another password(Y/N) = ")
    if d=='n' or d=='N':
        print("Your new passwors is : ",pat)
        break

print()

print("Thnks for using us")

