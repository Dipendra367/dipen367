import random


user_score=0
comp_score=0
ties=0

print("--------Welcome to rock paper and scissor game-------")
print()
print('''Chose the number for rock paper scissor
       1 for Rock
       2 for Papwe
       3 for Scissor''')
name=input("Enter your name to start the game : ")
print()
while True:
    choice=int(input('Enter the number : '))
    while choice>3 or choice<1:
        choice=int(input("Please enter the vaild choice(1-3) :"))

    print()
    if choice==1:
        user_choice='rock'
    elif choice==2:
        user_choice='paper'
    else:
        user_choice='scissor'

    print(name," choice is : ",user_choice)

    print()
    print("Now it's computer turn")
    print()
    rand=random.randint(1,3)
    if rand==1:
        comp_choice='rock'
    elif rand==2:
        comp_choice='paper'
    else:
        comp_choice ='scissor'

    print("Computer choice is : ",comp_choice)

    if (user_choice=='rock' and comp_choice=='paper') and (user_choice=='paper' and comp_choice=='rock'):
        print("paper win")
        result='paper'
    elif (user_choice=='rock' and comp_choice=='scissor') and (user_choice=='scissor' and comp_choice=='rock'):
        print("rock win")
        result='rock'
    elif comp_choice==user_choice:
        print("It's a Tie")
        result='tie'
    else:
        print("scissor win")
        result ='scissor'


    if result== 'tie':

        ties +=1
    elif result==user_choice:
        print(name," wins")
        user_score +=1

    else:
        print("computer wins")
        comp_score +=1

    print('SCORE ARE HERE')
    print("ties : ",ties)
    print(name," score is : ",user_score)
    print('computer score is :',comp_score)

    d=input("Do you wnat to play again?")
    if d=='n' or d=='N':
        break
print()
print("game over\t thnks for playing")