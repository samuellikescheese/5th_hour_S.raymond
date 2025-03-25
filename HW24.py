#Name:samuel
#Class: 5th Hour
#Assignment: HW24

import random, time

#1. Copy over your class from HW23 and all the functions inside of it, and alter any functions to use self if applicable.
class noob:
    def __init__ (self, health, damage, speed, max):
        self.health = health
        self.damage = damage
        self.speeed = speed
        self.max = max
    def cheese(self):
        for a in range(10):
            self.health -= random.randint(1, 6)
            time.sleep(1)
            print (self.health)
    def bees(self):
        self.health += 30
        if self.health >self.max:
            self.health = self.max
#2. Create a fourth attribute in the class called max_health that has the same values as health

#3. Copy the warrior and healer objects from HW23, and then make two more character objects with the following attribute values: thief (health/max: 50, damage: 30, speed: 40) and mage (health/max: 45, damage:35, speed: 25)
warrior = noob(100, 20, 30, 100)
healer = noob(60, 10, 30, 60)
thief = noob(50,30,40,50)
mage = noob(45,35,25,45)
#4. Randomly choose one of the four character objects to take the damage over time function and call the function to them
dice = random.randint(1,4)
if dice == 1:
    warrior.cheese()
if dice == 2:
    healer.cheese()
if dice == 3:
    thief.cheese()
if dice == 4:
    mage.cheese()
#5. Determine who lost health by comparing the current health to the max_health and heal that character object by calling your healing function to that object and then print their health afterwards.
if not warrior.health == warrior.max:
    warrior.bees()
    print (warrior.health)
if not healer.health == healer.max:
    healer.bees()
    print (healer.health)
if not thief.health == thief.max:
    thief.bees()
    print (thief.health)
if not mage.health == mage.max:
    mage.bees()
    print (mage.health)












