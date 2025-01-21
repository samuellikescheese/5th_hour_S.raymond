#Name:samuel raymond
#Class: 5th Hour
#Assignment: HW17

#1. Import the "random" library and create a def function that prints "Hello World!"
import random
def hello():
    print ("hello world")
#2. Create two empty integer variables named "heads" and "tails"
heads = 0
tails = 0
#3. Create a def function that flips a coin one hundred times and increments the result in the above variables.
def coin():
    global heads
    global tails
    end = 0
    while not end == 100:
        flip = random.randint(1, 2, )
        if flip == 1:
            heads += 1
            end += 1
        if flip == 2:
            tails += 1
            end += 1
#4. Call the "Hello world" and "Coin Flip" functions here
hello()
coin()
#5. Print the final result of heads and tails here
print(f"heads = {heads}")
print(f"tails = {tails}")






















