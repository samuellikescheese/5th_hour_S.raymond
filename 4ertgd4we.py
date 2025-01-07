import random
import time
print ("welcome to russian roulette")
print ("press 1 to play infinite mode")
print ("press 2 to play against a bot")
print ("press 3 to play against a player")
i = int(input(""))

#infinite mode
if i == 1:
    x = 0
    y = 0
    z = 0
    print ("welcome to infinite mode")
    while 5 > 3:
        input ()
        a = random.randint(1, 6, )
        print(a)
        if a == 1 :
            z += 1
            print ("you died")
            print(f"you got {x}")
            print(f"your highscore is {y}")
            print (f"your total death count is {z}")
            x = 0
            pass
        else :
            x += 1
            print (f"you survived for the {x} time")
            if x > y:
                y = x



#VS bot mode
if i == 2:
    print ("welcome to VS bot")
    play = 3
    bot = 3
    win = 0
    lose = 0
    while not play == 0 or bot == 0 :
        coin = random.randint(1, 2, )
        if coin == 1 :
            print ("heads")
        if coin == 2 :
            print ("tails")
        while coin == 1:
            a = random.randint(1, 6, )
            b = random.randint(1, 6, )
            print ("your turn")
            input ("")
            if a == 1 :
                print ("you get shot -1 health")
                play -= 1
                if play == 0:
                    print ("you died")
                    lose += 1
                    play = 3
                    bot = 3
                    print (f"bot has won {lose} times")
                    print(f"you have won {win} times")
                    continue
            else :
                print ("its a blank you are safe")
            print ("bots turn")
            time.sleep(1)
            if b == 1 :
                print  ("bot gets shot -1 health")
                bot -= 1
                if bot == 0:
                    print("bot died")
                    win += 1
                    play = 3
                    bot = 3
                    print(f"bot has won {lose} times")
                    print(f"you have won {win} times")
                    continue
            else :
                print ("its a blank bot is safe")
        while coin == 2:
            a = random.randint(1, 6, )
            b = random.randint(1, 6, )
            print ("bots turn")
            time.sleep(1)
            if b == 1 :
                print  ("bot gets shot -1 health")
                bot -= 1
                if bot == 0:
                    print("bot died")
                    win += 1
                    play = 3
                    bot = 3
                    print(f"bot has won {lose} times")
                    print(f"you have won {win} times")
                    continue
            else :
                print ("its a blank bot is safe")
            time.sleep(1)
            print ("your turn")
            input ("")
            if a == 1 :
                print ("you get shot -1 health")
                play -= 1
                if play == 0:
                    print("you died")
                    lose += 1
                    play = 3
                    bot = 3
                    print(f"bot has won {lose} times")
                    print(f"you have won {win} times")
                    continue
            else :
                print ("its a blank you are safe")



#VS player mode
if i == 3 :
    print ("welcome to VS player")
    play1 = 3
    play2 = 3
    while not play1 == 0 or play2 == 0 :
        coin = random.randint(1, 2, )
        if coin == 1 :
            print ("heads")
        if coin == 2 :
            print ("tails")
        while coin == 1:
            a = random.randint(1, 6, )
            b = random.randint(1, 6, )
            print ("player 1s turn")
            input ("")
            if a == 1 :
                print ("player 1 gets shot -1 health")
                play1 -= 1
                if play1 == 0:
                    print ("player 1 died")
                    play1 = 3
                    play2 = 3
                    continue
            else :
                print ("its a blank player 1 is safe")
            print ("player 2s turn")
            input("")
            if b == 1 :
                print  ("player 2 gets shot -1 health")
                play2 -= 1
                if play2 == 0:
                    print("bot died")
                    play1 = 3
                    play2 = 3
                    continue
            else :
                print ("its a blank player 2 is safe")
        while coin == 2:
            a = random.randint(1, 6, )
            b = random.randint(1, 6, )
            print ("player 2s turn")
            input("")
            if b == 1 :
                print  ("player 2 gets shot -1 health")
                play2 -= 1
                if play2 == 0:
                    print("player 2 died")
                    play1 = 3
                    play2 = 3
                    continue
            else :
                print ("its a blank player 2 is safe")
            time.sleep(1)
            print ("player 1s turn")
            input ("")
            if a == 1 :
                print ("player 1 gets shot -1 health")
                play1 -= 1
                if play1 == 0:
                    print("you died")
                    play1 = 3
                    play2 = 3
                    continue
            else :
                print ("its a blank player 1 is safe")







































