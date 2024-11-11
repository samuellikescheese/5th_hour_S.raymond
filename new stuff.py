import random
import time
x = 0
z = 0
while 5 > 3:
        ai = random.randint(1, 3)
        print ("rock = 1, paper = 2, scissers = 3")
        y = int(input())

        if y == 1:
            print ("you picked rock")
            if ai == 1:
                print ("ai picked rock")
                print ("TIE")
            if ai == 2:
                print("ai picked paper")
                print("AI WINS")
                z += 1
            if ai == 3:
                print("ai picked scissers")
                print("YOU WIN")
                x += 1

        if y == 2:
            print ("you picked paper")
            if ai == 1:
                print ("ai picked rock")
                print ("YOU WIN")
                x += 1
            if ai == 2:
                print("ai picked paper")
                print("TIE")
            if ai == 3:
                print("ai picked scissers")
                print("AI WINS")
                z += 1

        if y == 3:
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
        print (f"your score is {x}")
        print (f"ai score is {z}")






















































