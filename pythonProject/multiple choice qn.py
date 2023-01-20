#program to cretae multiple choice qns

print("----MCQS-----")
score=0

name=input("Enter you'r name to start the mcqs : ")
print()

print('''Here the rules:
        You got 10 questions and 4 option.
        Enter the correct option ex:-1 or 2 like that
        Total marks is 10 and pass marks is 5
        IF you get all correct you got a small prize
        But if got 5 you have pass the mcqs and no rewords
        And if you get less than 5 marks you fail.''')
print()
print('Here the questions goes:-')
print()

print('''A. What is capital city of Germany?
          1.Tokyo      2.Berlin
          3.Rome       4.Rio''')
inp1=int(input("Enter the correct option : "))
if inp1==2:
    print("Correct answer")
    score+=1

else:
    print("Incorrect answer")
    print("The correct answer is option 2 ")
print()
print('''B. What is the longest river in the world?
        1. Amazon river    2.Indus river
        3.Nile river      4.Congo river''')
inp1=int(input("Enter the correct option : "))
if inp1==3:
    print("Correct answer")
    score += 1


else:
    print("Incorrect answer")
    print("The correct answer is option 3")
print()



print('''C.When did the second world war started?
        1.1945       2.1917
        3.1939       3.1927''')
inp1=int(input("Enter the correct option : "))
if inp1==3:
    print("Correct answer")
    score += 1
else:
    print("Incorrect answer")
    print("The correct answer is option 3 ")
print()

print('''D. Who is also  known as the father of Math?
         1. Archimedes        2.Srinivasa Ramanujan
         3. G. H. Hardy       4.Aryabhata''')
inp1=int(input("Enter the correct option : "))
if inp1==1:
    print("Correct answer")
    score += 1
else:
    print("Incorrect answer")
    print("The correct answer is option 1")
print()
print('''E. Who invented the first alternating current (AC) motor ?
        1. Thomas Edison             2.Alexander Graham BelL
        3. Mabel Gardiner Hubbard    4.Nikola Tesla''')
inp1=int(input("Enter the correct option : "))
if inp1==4:
    print("Correct answer")
    score += 1
else:
    print("Incorrect answer")
    print("The correct answer is option 4 ")
print()

print('''F.Who was the the first human to travel into space ?
         1.Yuri Gagarin     2.Neil Armstrong
         3.Buzz Aldrin      4.Michael Collins''')
inp1=int(input("Enter the correct option : "))
if inp1==1:
    print("Correct answer")
    score += 1
else:
    print("Incorrect answer")
    print("The correct answer is option 1 ")
print()
print('''G.Whic country won the first world cup?
        1.Argentina    2.Uruguya
        3.Brazil       4.Italy''')
inp1=int(input("Enter the correct option : "))
if inp1==2:
    print("Correct answer")
    score += 1
else:
    print("Incorrect answer")
    print("The correct answer is option 2 ")
print()
print('''H.What is the molecular formula of formic acid?
        1.HCO2H       2.HCOOH
        3.C₆H₈O₇      4.CH₂O₂''')
inp1=int(input("Enter the correct option : "))
if inp1==4:
    print("Correct answer")
    score += 1
else:
    print("Incorrect answer")
    print("The correct answer is option 4")
print()
print('''I.What was the main electronic component of second-generation computer systems?
         1.IC          2.Vaccum Tubes
         3.Transistor  4.Microprocessor ''')
inp1=int(input("Enter the correct option : "))
if inp1==3:
    print("Correct answer")
    score += 1
else:
    print("Incorrect answer")
    print("The correct answer is option 3 ")
print()
print('''J.Who gave the famous speech "I Have A DREAM"
        1.Malcolm X            2.Martin Luther King Jr
        3.Nelson Mandela       4.John F. Kennedy''')
inp1=int(input("Enter the correct option : "))
if inp1==2:
    print("Correct answer")
    score += 1

else:
    print("Incorrect answer")
    print("The correct answer is option 2 ")
print()

print(name,"you'r score is : " , score)

if score==10:
    print(name,'Congrass you got all answer right.')
    print("Now you will win one reward")

elif score>=5 or score<10:
    print(name,"Congrass you pass the quize")

else:
    print(name,"Sorry you will")

print()

print('''===========================================================
                    Thanku for participate in the MCQS
         =============================================================''')


