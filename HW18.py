#Name:samuel raymond
#Class: 5th Hour
#Assignment: HW18


#1. Import the "random" library and create a def function that prints "Hello World!"
import random
def hello():
    print ("hello world")
#2. Create a list called beanBag and add at least 5 different colored beans to the list as strings.
beanbag = ["blue","red","yellow","green","purple"]
#3. Create a def function that pulls a random bean out of the beanBag list, prints which bean you pulled, and then removes it from the list.
xa = 4
def graby():
    pullbean = random.choice(beanbag)
    print (pullbean)
    beanbag.remove(pullbean)
    again()
#4. Create a def function that asks if you want to pull another bean out of the bag and, if yes, repeats the #3 def function
def again():
    x = (input())
    if x == "y":
        graby()
    elif x == "n":
        exit()
    else:
        print ("error")
        again()
#5. Call the #3 function at the bottom.
graby()
























