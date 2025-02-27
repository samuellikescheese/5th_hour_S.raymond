import random
x = 0
y = 0
z = 0
win = 0
lose = 0
play = 3
bolt = 3
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
                    if g == "n":
                        game()
                    else:
                        infinite()
                again()
            else:
                x += 1
                print (f"you survived for the {x} time")
                if x > y:
                    y = x
#VS bot

game()

































