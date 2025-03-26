#Name: samuel
#Class: 5th Hour
#Assignment: Scenario8
#Scenario 8:
#With a fresh perspective, the team lead wants you to look back and refactor the old combat code to
#be streamlined with classes so the character and enemy stats won't be built in bulky dictionaries anymore.
#(Translation: Rebuild Scenario 3 using classes instead of dictionaries, include the combat test code
#below as well.)
import random

print("hello world")
# the good guys
class noob:
    def __init__ (self, roll, health, AC, damage ):
        self.health = health
        self.damage = damage
        self.roll = roll
        self.AC = AC
gale = noob(4, 8, 14, random.randint(1,10))
white = noob(3, 8, 14, random.randint(1,4) + 1)
black = noob(3,12,14, random.randint(1,8) + 2)
green = noob(3,14,14,random.randint(1,10) + 3)
blue = noob(3,16, 14,random.randint(1,12) + 4)
red = noob(3,18, 14,random.randint(1,20) + 5)



print ("you play as gale the heroo")
print ("your enemy is the white dragon (kill it)")
print ("gale attacks the dragon")
if random.randint(1, 20) + gale.roll >= (white.AC):
    white.health -= gale.damage
    if white.health <= 0:
        print ("the white dragon is dead")
        exit()
    else:
        print ("the dragon stands")
else :
    print ("he misses")
print ("the dragon attacks")
if random.randint(1, 20) + white.roll >= gale.AC :
    gale.health -= white.roll
    if gale.health <= 0:
        print ("gale is dead")
        exit()
    else:
        print ("gale stands")
else :
    print ("he misses")



