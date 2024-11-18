import random
import time

r = 0
b = 0
y = 0
while not r == 10 and not y == 10 and not b == 10 :
    red = random.randint(1, 10,)
    blue = random.randint(1, 10,)
    yellow = random.randint(1, 10,)
    time.sleep(0.1)
    if yellow > red and yellow > blue:
        print ("yellow wins")
        y += 1
    elif red > blue and red > yellow:
        print ("red wins")
        r += 1
    elif blue > red and blue > yellow:
        print ("blue wins")
        b += 1
    elif yellow > blue and red > blue:
        print ("yellow and red win")
        r += 1
        y += 1
    elif blue > yellow and red > yellow:
        print ("red and blue win")
        r += 1
        b += 1
    elif yellow > red and blue > red:
        print ("yellow and blue win")
        b += 1
        y += 1
    else:
        print ("all equal")
        b += 1
        r += 1
        y += 1
    print (f"red = {red} and has {r} wins")
    print (f"yellow = {yellow} and has {y} wins")
    print (f"blue = {blue} and has {b} wins")
if r == 10 and y == 10 and b == 10:
    print ("red, blue, and yellow win")
elif r == 10 and y == 10:
    print ("red and yellow win")
elif b == 10 and y == 10:
    print ("blue and yellow win")
elif r == 10 and b == 10:
    print ("red and blue win")
elif r == 10:
    print ("red wins")
elif b == 10:
    print ("blue wins")
elif y == 10:
    print ("yellow wins")




