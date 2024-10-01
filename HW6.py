#samuel raymond
#5th
#HW6

print("hello world")
num = int(input())

if num % 2 == 0:
    if num % 3 == 0:
        print("your number is divesible by 2")
        x = num / 2
        print (f"{num} / 2 = {x}")
        print("your number is divesible by 3")
        y = num / 3
        print (f"{num} / 3 = {y}")
    else:
        print("it is not divesible by 3")
        print("your number is divesible by 2")
        x = num / 2
        print(f"{num} / 2 = {x}")
else :
    if num % 3 == 0 :
        print("your number is divesible by 3")
        y = num / 3
        print (f"{num} / 3 = {y}")
        print("it is not divesible by 2")
    else :
        print("it is not divesible by 2 or 3")


















