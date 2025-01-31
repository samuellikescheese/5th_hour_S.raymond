import random
x = 0
y = 0
z = 0
win = 0
lose = 0
play = 3
bot = 3
def game():
    print ("welcome to russian roulette")
    print ("press 1 to play infinite mode")
    print ("press 2 to play against a bot")
    print ("press 3 to play against a player")
    i = int(input(""))

#infinite mode
    def infinite():
        global x
        global y
        global z
        print ("welcome to infinite mode")
        while 5 > 3:
            input ()
            a = random.randint(1, 6, )
            print(a)
            if a == 1 :
                z += 1
                print ("you died")
                print (f"you got {x}")
                print (f"your highscore is {y}")
                print (f"your total death count is {z}")
                x = 0
                def again():
                    print ("do you want to play again?")
                    print ("y = yes")
                    print("n = no")
                    g = input("")
                    if g == "y":
                        infinite()
                    elif g == "n":
                        game()
                    else:
                        print ("error")
                        again()
                again()
            else :
                x += 1
                print (f"you survived for the {x} time")
                if x > y:
                    y = x
#VS bot
    def bot():
        global bot
        global play
        global lose
        global win
        print("welcome to VS bot")
        while not play == 0 or bot == 0:

            def player():
                global bot
                global play
                global lose
                global win
                a = random.randint(1, 6, )
                print("your turn")
                input("")
                if a == 1:
                    print("you get shot -1 health")
                    play -= 1
                    if play == 0:
                        print("you died")
                        lose += 1
                        play = 3
                        bot = 3
                        print(f"bot has won {lose} times")
                        print(f"you have won {win} times")
                    else:
                        bot()
            def bot():
                global bot
                global play
                global lose
                global win
                b = random.randint(1, 6, )
                print("bots turn")
                if b == 1:
                    print("bot gets shot -1 health")
                    bot -= 1
                    if bot == 0:
                        print("bot died")
                        win += 1
                        play = 3
                        bot = 3
                        print(f"bot has won {lose} times")
                        print(f"you have won {win} times")
            coin = random.randint(1, 2, )
            if coin == 1:
                print("heads")
                player()
            if coin == 2:
                print("tails")
                bot()
    if i == 1:
        infinite()
    elif i == 2:
        bot()
game()

































