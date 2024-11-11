#samuel raymond
#5th
#playground
import random
import time
print("hello world")
while 5 > 3:
    time.sleep(2)
    print ("1 = add")
    print ("2 = minus")
    print ("3 = mult")
    print ("4 = divide")
    print ("5 = exponent")
    a = random.randint(1, 5)


    if a == 1:
        print ("you picked add")
        print("Enter 2 Numbers")
        x = random.randint(-100, 100)
        y = random.randint(-100, 100)
        print (x)
        print (y)
        plus = (x + y)
        print (f"Your Answer is {plus} ")
    if a == 2:
        print("you picked minus")
        print("Enter 2 Numbers")
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        print(x)
        print(y)
        plus = (x - y)
        print (f"Your Answer is {plus} ")
    if a == 3:
        print("you picked mult")
        print("Enter 2 Numbers")
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        print(x)
        print(y)
        plus = (x * y)
        print (f"Your Answer is {plus} ")
    if a == 4:
        print("you picked divide")
        print("Enter 2 Numbers")
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        print(x)
        print(y)
        plus = (x / y)
        print (f"Your Answer is {plus} ")
    if a == 5:
        print("you picked exponent")
        print("Enter 2 Numbers")
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        print(x)
        print(y)
        plus = (x ** y)
        print(f"Your Answer is {plus} ")


