import random
import time
time = 0
w = 0
x = 0
z = 0
while 5 > 3:
        ai = random.randint(1, 3)
        print ("rock = 1, paper = 2, scissers = 3")
        y = int(input())

        if y == 1:
            time += 1
            print ("you picked rock")
            if ai == 1:
                print ("ai picked rock")
                print ("TIE")
                w += 123
            if ai == 2:
                print("ai picked paper")
                print("AI WINS")
                z += 1
            if ai == 3:
                print("ai picked scissers")
                print("YOU WIN")
                x += 1

        if y == 2:
            time += 1
            print ("you picked paper")
            if ai == 1:
                print ("ai picked rock")
                print ("YOU WIN")
                x += 1
            if ai == 2:
                print("ai picked paper")
                print("TIE")
                w += 1
            if ai == 3:
                print("ai picked scissers")
                print("AI WINS")
                z += 1

        if y == 3:
            time += 1
            print ("you picked scissers")
            if ai == 1:
                print("ai picked rock")
                print("AI WINS")
                z += 1
            if ai == 2:
                print("ai picked paper")
                print("YOU WIN")
                x += 1
            if ai == 3:
                print("ai picked scissers")
                print("TIE")
                w += 1
        if not y == 1 and not y == 2 and not y == 3:
            print ("pick a number stupid")
        print (f"your score is {x}")
        print (f"ai score is {z}")
        print (f"there are {w} ties")
        print (f"{time} games")






















































