#samuel raymond
#5th
#HW6
import random

print("hello world")
# the good guys
partyDictionary = {
    "LaeZel" : {
        "roll": 2,
        "Health" : 12,
        "AC" : 17,
        "Damage" :random.randint(1,6) + random.randint(1,6) + 3 ,
    },
    "Shadowheart" : {
        "roll": 2,
        "Health" : 10,
        "AC" : 14,
        "Damage" : random.randint(1,6) + 2,
    },
    #i  pick this one
    "Gale" : {
        "roll": 4,
        "Health" : 8,
        "AC" : 14,
        "Damage" : random.randint(1,10),
    },
    "Astarion" : {
        "roll" : 3,
        "Health" : 10,
        "AC" : 14,
        "Damage" : random.randint(1,6) + 2,
     },
}
# the bad guys
dragons = {
    #i  pick this one
    "white" : {
        "roll": 3,
        "Health": 8,
        "AC": 14,
        "Damage": random.randint(1, 4) + 1,
    },
    "black": {
        "roll": 3,
        "Health": 12,
        "AC": 14,
        "Damage": random.randint(1, 6) + 2,
    },
    "green": {
        "roll": 3,
        "Health": 14,
        "AC": 14,
        "Damage": random.randint(1, 10) + 3,
    },
    "blue": {
        "roll": 3,
        "Health": 16,
        "AC": 14,
        "Damage": random.randint(1, 12) + 4,
    },
    "red": {
        "roll": 3,
        "Health": 18,
        "AC": 14,
        "Damage": random.randint(1, 20) + 5,
    }
}
#Now that the game development team has a dictionary for enemies
#(see Scenario 1) and the dictionary for the party is fixed
#(see Scenario 2), they want to start making a full prototype for the
#combat system. The team lead is a big Dungeons & Dragons fan and
#wants to make the combat similar to that. Because of this, the
#dictionaries need to be reworked slightly to be like that.

#Each enemy and party member in both dictionaries needs:
# - health points (somewhere between 6 and 25)
# - an attack modifier (somewhere between 3 and 7)
# - a damage roll (a number that varies based on weapon/spell)
# - and an Armor Class (somewhere between 10 and 17).

#Once both dictionaries are updated, create a combat
#prototype that has a party member attack first, then an enemy
#attacks back right after.

#To determine if a creature hits another creature, you roll a
#20-sided die (d20) and add the attack modifier to the roll.
#If that number is the same as or higher than the enemy's Armor Class
#(AC), the attack hits and you roll for damage. If it is lower, the
#attack misses. If an enemy or party member hits zero (0) health
#points, they die.

#To make things easier, here is a reference list for party damage rolls.
#(Feel free to use similar numbers for your enemy dictionary.)

# - Lae'Zel uses a greatsword: 2d6 + 3
# - Shadowheart uses a mace: 1d6 + 2
# - Gale uses the firebolt spell: 1d10
# - Astarion uses a shortbow: 1d6 + 4
print ("you play as gale the hero")
print ("your enemy is the white dragon (kill it)")
print ("gale attacks the dragon")
if random.randint(1, 20) + partyDictionary["Gale"]["roll"] >= (dragons["white"]["AC"]):
    dragons["white"]["Health"] -= partyDictionary["Gale"]["Damage"]
    if dragons["white"]["Health"] <= 0:
        print ("the white dragon is dead")
        exit()
    else:
        print ("the dragon stands")
else :
    print ("he misses")
print ("the dragon attacks")
if random.randint(1, 20) + (dragons["white"]["roll"] >=partyDictionary["Gale"]["AC"] ):
    partyDictionary["Gale"]["Health"] -= dragons["white"]["roll"]
    if partyDictionary["Gale"]["Health"] <= 0:
        print ("gale is dead")
        exit()
    else:
        print ("gale stands")
else :
    print ("he misses")














































































