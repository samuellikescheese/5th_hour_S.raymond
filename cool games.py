#sams house
import random
def dice() :
    input()
    a1 = random.randint(1, 6, )
    a2 = random.randint(1, 6, )
    a3 = random.randint(1, 6, )
    a4 = random.randint(1, 6, )
    a5 = random.randint(1, 6, )
    print(a1)
    print(a2)
    print(a3)
    print(a4)
    print(a5)
    if a1 == a2 == a3 == a4 == a5:
        print ("quintuple")
    elif a1==a2==a3==a4 or a5==a2==a3==a4 or a1==a5==a3==a4 or a1==a2==a5==a4 or a1==a2==a3==a5:
        print ("quadruple")
    elif a1==a2==a3 or a2==a3==a4 or a3==a4==a5 or a4==a5==a1 or a3==a4==a1 or a4==a1==a2 or a5==a2==a3 or a5==a1==a2 or a5==a3==a1 or a5==a2==a4:
        print ("triple")
    elif a1==a2 and a3==a4 or a2==a3 and a1==a4 or a2==a4 and a3==a4 or a5==a1 and a4==a3 or a5==a1 and a4==a2 or a5==a1 and a3==a2 or a5==a2 and a3==a1 or a5==a2 and a4==a1 or a5==a2 and a4==a3 or a5==a3 and a4==a2 or a5==a3 and a4==a1 or a5==a3 and a2==a1 :
        print ("double double")
    elif a1==a2 or a2==a3 or a3==a1 or a1==a4 or a2==a4 or a3==a4 or a5==a3 or a5==a1 or a5==a4 or a2==a5:
        print ("double")
    else:
        print ("nothing")
    dice()
dice()


























