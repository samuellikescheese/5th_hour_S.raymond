#sams house
import random

nothing = 0
double = 0
doubledouble = 0
triple = 0
tripledouble = 0
quadruple = 0
quintuple = 0
def dice() :
    global nothing
    global double
    global doubledouble
    global triple
    global tripledouble
    global quadruple
    global quintuple
    x = input()
    a1 = random.randint(1, 6, )
    a2 = random.randint(1, 6, )
    a3 = random.randint(1, 6, )
    a4 = random.randint(1, 6, )
    a5 = random.randint(1, 6, )
    if x == "p":
        print (f"double = {double}")
        print (f'double,double = {doubledouble}')
        print (f"triple = {triple}")
        print (f"nothing = {nothing}")
        print (f"triple,double = {tripledouble}")
        print (f"quadruple = {quadruple}")
        print (f"quintuple = {quintuple}")
        dice()
    print(f"{a1},{a2},{a3},{a4},{a5}")
    if a1 == a2 == a3 == a4 == a5:
        print ("quintuple")
        quintuple += 1
    elif a1==a2==a3==a4 or a5==a2==a3==a4 or a1==a5==a3==a4 or a1==a2==a5==a4 or a1==a2==a3==a5:
        print ("quadruple")
        quadruple += 1
    elif a1==a2==a3 and a4==a5 or a2==a3==a4 and a5==a1 or a3==a4==a5 and a1==a2 or a4==a5==a1 and a2==a3 or a5==a1==a2 and a3==a4 or a1==a2==a4 and a3==a5 or a1==a5==a3 and a2==a4 or a4==a5==a2 and a1==a3 or a5==a2==a3 and a1==a4 or a4==a3==a1 and a5==a2:
        print ("triple,double")
        tripledouble += 1
    elif a1==a2==a3 or a2==a3==a4 or a3==a4==a5 or a4==a5==a1 or a3==a4==a1 or a4==a1==a2 or a5==a2==a3 or a5==a1==a2 or a5==a3==a1 or a5==a2==a4:
        print ("triple")
        triple += 1
    elif a1==a2 and a3==a4 or a2==a3 and a1==a4 or a2==a4 and a3==a4 or a5==a1 and a4==a3 or a5==a1 and a4==a2 or a5==a1 and a3==a2 or a5==a2 and a3==a1 or a5==a2 and a4==a1 or a5==a2 and a4==a3 or a5==a3 and a4==a2 or a5==a3 and a4==a1 or a5==a3 and a2==a1 or a5==a4 and a3==a2 or a5==a4 and a2==a1 or a5==a4 and a3==a1 :
        print ("double,double")
        doubledouble += 1
    elif a1==a2 or a2==a3 or a3==a1 or a1==a4 or a2==a4 or a3==a4 or a5==a3 or a5==a1 or a5==a4 or a2==a5:
        print ("double")
        double += 1
    else:
        print ("nothing")
        nothing += 1
    dice()
dice()


























