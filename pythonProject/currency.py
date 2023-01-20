#currency converter

print('''Here you convert any currency into nepali
        here are following country currency we converted :
        1.America(dollor)   6.Austrila        11.U.A.E
        2.Uk(pound)         7.Quatar          12.Canada
        3.Europe(euro)      8.Saudi Arabia    13.Malaysia
        4.Japan(yen)        9. Korea          14.Russia
        5.India(rupees)     10.Kuwait         15.Singapore''')
print()


print("Select the number that represent the country in the list above")
while True:
    num=int(input("Enter the the number of amount you want to convert : "))
    inp=int(input("Select the number of the country shown in the list above : "))

    if inp==1:
        c=num/130.15
        print(str(num) + "rs  in dollor is : " + str(c))
    elif inp==2:
        c = num / 160.75
        print(str(num) + " rs in pound is : " + str(c))
    elif inp==3:
        c = num / 140.61
        print(str(num) + " rs in euron is : " + str(c))

    elif inp==4:
        c = num / 1.01
        print(str(num) + " rs in yen is : " + str(c))
    elif inp==5:
        c = num / 1.60
        print(str(num) + " rs in indian rupees is : " + str(c))
    elif inp==6:
        c = num / 89.80
        print(str(num) + " rs in austrilian dollor is : " + str(c))
    elif inp==7:
        c = num / 35.74
        print(str(num) + " rs in qatari riyal is : " + str(c))
    elif inp==8:
        c = num / 34.65
        print(str(num) + " rs  saudi riyal is : " + str(c))
    elif inp==9:
        c = num / 0.11
        print(str(num) + " rs  korean won  is : " + str(c))
    elif inp==10:
        c = num / 426.11
        print(str(num) + " rs  kuwait diner is : " + str(c))
    elif inp==11:
        c = num / 35.43
        print(str(num) + " rs  U.A.E dihram is : " + str(c))
    elif inp==12:
        c = num / 96.59
        print(str(num) + " rs  canadian dollor is : " + str(c))
    elif inp==13:
        c = num / 30.21
        print(str(num) + " rs  malaysian ringgit is : " + str(c))
    elif inp==14:
        c = num / 1.89
        print(str(num) + " rs  russia rubble is : " + str(c))
    elif inp==15:
        c = num / 98.28
        print(str(num) + " rs in singaporea dollor is : " + str(c))

    else:
        print("sorry we only have limited countries only we will add soon other countries curency too")

    rep=input("Do you wnat to see aother country ?")
    if rep=='n'or rep=='N':
        break

print("Thanku :))")



