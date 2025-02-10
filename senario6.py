#Name:samuel raymond
#Class: 5th Hour
#Assigment: Scenario 6
import random
import time

#After an extended leave, the team lead for the RPG developer is back, and he wants to continue the project.
#He wants to prototype the character creation model but first needs something that rolls stats for the characters.
#He wants you to make a function that rolls 4 six-sided dice (d6), sorts them from highest to lowest, and then adds the
#highest 3 together. He then wants you to add that result to a list outside the function. He wants you to run that function
#5 more times (six times total) and print all six stats.

#Once that is done, to ensure that the average of the statblock is fair (somewhere roughly between 12-13), he wants you
#to plug it into a calculator (Scenario 7) and print the average.
play = []
def roll():
    x = 0
    while not x == 6:
        d1 = random.randint(1, 6, )
        d2 = random.randint(1, 6, )
        d3 = random.randint(1, 6, )
        d4 = random.randint(1, 6, )
        guy = [d1,d2,d3,d4]
        small = min(guy)
        print (small)
        guy.remove(min(guy))
        print(sum(guy))
        play.append(sum(guy))
        x += 1
        time.sleep(0.5)
    print (play)
roll()













