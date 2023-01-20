#tiger and goat game
import random

print('-----WELCOME  TO TIGER AND HUNTER  GAME---------')

print(''' In this game you have to choose either Tiger or HUNTER
       here the rules:
       If you choose Tiger then you must be able to guess the number that is chosen by the hunter
        if you not then you die
        But if choose hunter then  by default
        you'r number is 3 if tiger choose the number that is bigger than 3 you win
        but if tiger choose the number that is smaller  than 3 then you die
        if tiger also choose 3 then again you die
        if you want to  win then tiger must choose the bigger number than 3. ''')
print()

print("You can choose either Tiger or Hunter.")
print()
while True:

    choose=input("Please enter 'T' OR 't' to be a tiger and enter 'H' OR 'h' to be a hunter =")
    if choose=='T' or choose =='t':
        print("OK you choose a Tiger")
        print("Now you are a Tiger")
        num1=int(input("please choose aright number that is choosen by hunter (1-5) : "))
        rand=random.randint(1,5)
        print("And the hunter choose : ",rand)
        if rand==num1:
            print("Congras you killed the hunter :)")
            print("Now you are safe")
        else:
            print("O no your are being killed by the hunter :(")

    elif choose=='h'or choose=='H':
        print("Ok you choose a hunter")
        print("Now you are a hunter")
        print("It's means by deafult you'r number is three you cab't chhose the number")
        print("You'r number is = 3")

        rand2=random.randint(1,5)
        print("And tiger choose = ",rand2)
        if 3<rand2:
            print("Congarss you killed the tiger :)")
        else:
            print("O no you are being killed by the tiger :(")

    else:
        print("Please choose the valid word(T OR t  and H OR h)")
    d=input('Do you wnat to play againn (Y/N)?')
    if d=='n' or d=='N':
        break


print()
print()
print("Thnks for playing our game")




