#samuel raymond
#5th
#HW6

print("hello world")
num = int(input())

if num % 2 == 0:
    if num % 3 == 0:
        if num % 5 == 0:
            print("your number is divesible by 2")
            x = num / 2
            print(f"{num} / 2 = {x}")
            print("your number is divesible by 3")
            y = num / 3
            print(f"{num} / 3 = {y}")
            print("your number is divesible by 5")
            z = num / 5
            print(f"{num} / 3 = {z}")
        else:
            print("it is not divesible by 5")
            print("your number is divesible by 2")
            x = num / 2
            print (f"{num} / 2 = {x}")
            print("your number is divesible by 3")
            y = num / 3
            print (f"{num} / 3 = {y}")
    else:
        if num % 5 == 0 :
            print("it is not divesible by 3")
            print("your number is divesible by 2")
            x = num / 2
            print(f"{num} / 2 = {x}")
            print("your number is divesible by 5")
            z = num / 5
            print(f"{num} / 5 = {z}")
        else :
            print("it is not divesible by 3")
            print("your number is divesible by 2")
            x = num / 2
            print(f"{num} / 2 = {x}")
            print("it is not divesible by 5")
elif num % 3 == 0 :
    if num % 5 == 0:

        print("your number is divesible by 3")
        y = num / 3
        print(f"{num} / 3 = {y}")
        print("it is not divesible by 2")
        print("your number is divesible by 5")
        z = num / 5
        print(f"{num} / 5 = {z}")
    else:
        print("your number is divesible by 3")
        y = num / 3
        print (f"{num} / 3 = {y}")
        print("it is not divesible by 2")
        print("it is not divesible by 5")
elif num % 5 == 0 :
    print ("your number is divesible by 5")
    z = num / 5
    print(f"{num} / 5 = {z}")
    print("it is not divesible by 3")
    print("it is not divesible by 2")
else :
    print("it is not divesible by 2 or 3 or 5")


















