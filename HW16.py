#Name:samuel raymond
#Class: 5th Hour
#Assignment: HW16
import random
def end():
    x = int(input())
    if x == 1:
        game()
    else:
        exit()
#1. Create a def function that plays a single round of rock, paper, scissors where the user inputs
#1 for rock, 2 for paper, or 3 for scissors and compares it to a random number generated to serve
#as the "opponent's hand".
def game():
    play = int(input())
    bot = random.randint(1, 3, )
    if play == 1:
        print ("you picked rock")
        if bot == 1:
            print("bot picked rock")
            print ("tie")
        if bot == 2:
            print("bot picked paper")
            print("you lose")
        if bot == 3:
            print("bot picked scissors")
            print("you win")
    if play == 2:
        print ("you picked paper")
        if bot == 1:
            print("bot picked rock")
            print("you win")
        if bot == 2:
            print("bot picked paper")
            print("tie")
        if bot == 3:
            print("bot picked scissors")
            print("you lose")
    if play == 3:
        print ("you picked scissors")
        if bot == 1:
            print("bot picked rock")
            print("you lose")
        if bot == 2:
            print("bot picked paper")
            print("you win")
        if bot == 3:
            print("bot picked scissors")
            print("tie")

    end()
game()
#2. Create a def function that prompts the user to input if they want to play another round, and
#repeats the RPS def function if they do or exits the code if they don't.
















