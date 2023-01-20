#Guess the number project

import random

print("------------Welcome to our Game-------------")

name=input("Enter your name to start the game : ")
print()

print('''Here the absic game rule:
         You enetr any number and that number match the number that is 
         randomly generate by the cimputer you won the game''')
while True:
    num=int(input("Enter the number (1-10) : "))

    while num>10 or num<1 :
        num=int(input('Please enter the valid number : '))

    print()
    print("Now its computer turn")

    comp=random.randint(1,10)
    print("The number generate by the computer iss : " + str(comp))

    if num==comp:
        print(name ,  " Congars you guess right number" )
    else:
        print("Keep trying...")

    d=input("Do you want to try again ?")
    if d=='n' or d=='N':
        break
    print()

print("Game over")
print("Thanks for playing", name)