# creating calculator
while True:
    num1=int(input("Enter your first number :"))
    num2=int(input("Enter your second number : "))

    print('''Select the following number to perform the operation
            + for Addition
            - for substraction
            * for multiplicatin
            / for the division''')

    print()



    char=input("Enter the following sign that mention above:  ")



    if char == '+':
        c=num1+num2
        print("The addition of that number is :" + str(c) )

    elif char == "-":
        c=num1-num2
        print("The subtraction of that number is :" + str(c))


    elif char =='*':
        c=num1*num2
        print("The multiplicatin of that number is :" + str(c))
    elif char =="/":
        c=num1/num2
        print("The division of that number is :" + str(c))
    else:
        print("You enetr the wrong operator....")


    d=input("Do you want o repaet the task?")
    if d=='n' or d=="N":
        break

print()

print("Thanku ")
