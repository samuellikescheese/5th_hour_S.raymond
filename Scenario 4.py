#Name: samuel
#Class: 5th Hour
#Assignment: sen4
import random
x = 0
print ("hello world")
while 5 > 3:
    print ("input how many players you have (more then 0)")
    players = int(input(""))
    if players < 1:
        print ("more then 0 stupid")
        continue
    count = players
    while not players == 0:
        print ("input your score (1-5)")
        score = int(input(""))
        if score > 5 or score < 1 :
            print ("1 tho 5 stupid")
            continue
        players -= 1
        x += score
        print (score)
    y = x / count
    print (y)

#cheese
#Scenario 4:
#Due to scope creep leading to high development costs, the RPG you were working on has been
#shelved for the time being. You have been transferred to a new team working on a mobile game
#that allows you to dress up a model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.














