import random
import time
x = 0
y = 0
while 5 > 3:
    input ()
    a = random.randint(1, 6, )
    print(a)
    if a == 1 :
        print ("you died")
        print(f"you got {x}")
        print(f"your highscore is {y}")
        x = 0
        pass
    else :
        x += 1
        print (f"you survived for the {x} time")
        if x > y:
            y = x








































