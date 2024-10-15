#samuel raymond
#5th
#HW6

print("hello world")
num = int(input())

if num % 2 == 0:
    if num % 3 == 0:
        if num % 5 == 0:
            if num % 7 == 0:
                print("your number is divesible by 2")
                x = num / 2
                print(f"{num} / 2 = {x}")
                print("your number is divesible by 3")
                y = num / 3
                print(f"{num} / 3 = {y}")
                print("your number is divesible by 5")
                z = num / 5
                print(f"{num} / 5 = {z}")
            else:
                print("your number is divesible by 2")
                x = num / 2
                print(f"{num} / 2 = {x}")
                print("your number is divesible by 3")
                y = num / 3
                print(f"{num} / 3 = {y}")
                print("your number is divesible by 5")
                z = num / 5
                print(f"{num} / 5 = {z}")
                print("it is not divesible by 7")
            print("your number is divesible by 2")
            x = num / 2
            print(f"{num} / 2 = {x}")
            print("your number is divesible by 3")
            y = num / 3
            print(f"{num} / 3 = {y}")
            print("your number is divesible by 5")
            z = num / 5
            print(f"{num} / 5 = {z}")
        else:
            if num % 7 == 0:
                print("your number is divesible by 2")
                x = num / 2
                print(f"{num} / 2 = {x}")
                print("your number is divesible by 3")
                y = num / 3
                print(f"{num} / 3 = {y}")
                print("your number is divesible by 7")
                w = num / 7
                print(f"{num} / 7 = {w}")
                print("it is not divesible by 5")
            else :
                print("your number is divesible by 2")
                x = num / 2
                print (f"{num} / 2 = {x}")
                print("your number is divesible by 3")
                y = num / 3
                print (f"{num} / 3 = {y}")
                print("it is not divesible by 5")
                print("it is not divesible by 7")
    else:
        if num % 5 == 0 :
            if num % 7 == 0:
                print("your number is divesible by 2")
                x = num / 2
                print(f"{num} / 2 = {x}")
                print("your number is divesible by 5")
                z = num / 5
                print(f"{num} / 5 = {z}")
                print("your number is divesible by 7")
                w = num / 7
                print(f"{num} / 7 = {w}")
            else:
                print("your number is divesible by 2")
                x = num / 2
                print(f"{num} / 2 = {x}")
                print("your number is divesible by 5")
                z = num / 5
                print(f"{num} / 5 = {z}")
                print("it is not divesible by 3")
                print("it is not divesible by 7")
        else :
            if num % 7 == 0:
                print("your number is divesible by 2")
                x = num / 2
                print(f"{num} / 2 = {x}")
                print("your number is divesible by 7")
                w = num / 7
                print(f"{num} / 7 = {w}")
                print("it is not divesible by 3")
                print("it is not divesible by 5")
            else:
                print("your number is divesible by 2")
                x = num / 2
                print(f"{num} / 2 = {x}")
                print("it is not divesible by 3")
                print("it is not divesible by 5")
                print("it is not divesible by 7")
elif num % 3 == 0 :
    if num % 5 == 0:
        if num % 7 == 0:
            print("your number is divesible by 3")
            y = num / 3
            print(f"{num} / 3 = {y}")
            print("your number is divesible by 5")
            z = num / 5
            print(f"{num} / 5 = {z}")
            print("your number is divesible by 7")
            w = num / 7
            print(f"{num} / 7 = {w}")
            print("it is not divesible by 2")
        else:
            print("your number is divesible by 3")
            y = num / 3
            print(f"{num} / 3 = {y}")
            print("your number is divesible by 5")
            z = num / 5
            print(f"{num} / 5 = {z}")
            print("it is not divesible by 2")
            print("it is not divesible by 7")
    else:
        if num % 7 == 0:
            print("your number is divesible by 3")
            y = num / 3
            print(f"{num} / 3 = {y}")
            print("your number is divesible by 7")
            w = num / 7
            print(f"{num} / 7 = {w}")
            print("it is not divesible by 2")
            print("it is not divesible by 5")
        else:
            print("your number is divesible by 3")
            y = num / 3
            print (f"{num} / 3 = {y}")
            print("it is not divesible by 2")
            print("it is not divesible by 5")
            print("it is not divesible by 7")
elif num % 5 == 0 :
    if num % 7 == 0:
        print("your number is divesible by 5")
        z = num / 5
        print(f"{num} / 5 = {z}")
        print("your number is divesible by 7")
        w = num / 7
        print(f"{num} / 7 = {w}")
        print("it is not divesible by 2")
        print("it is not divesible by 3")
    else:
        print ("your number is divesible by 5")
        z = num / 5
        print(f"{num} / 5 = {z}")
        print("it is not divesible by 2")
        print("it is not divesible by 3")
        print("it is not divesible by 7")
elif num % 7 == 0:
    print("your number is divesible by 7")
    w = num / 7
    print(f"{num} / 7 = {w}")
    print("it is not divesible by 2")
    print("it is not divesible by 3")
    print("it is not divesible by 5")
else :
    print("it is not divesible by 2")
    print("it is not divesible by 3")
    print("it is not divesible by 5")
    print("it is not divesible by 7")


















