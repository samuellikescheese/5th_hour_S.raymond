#Name:samuel
#Class: 5th Hour
#Assignment: HW20
from logging import raiseExceptions

#1. Create a try catch that tries to print variable x (which has no value), but prints "Hello World!" instead.
try:
    print (x)
except:
    print ("hello world")
#2. Create a try catch that tries to divide 100 by whatever number the user inputs, but prints an exception for Divide By Zero errors.
y = int(input())
try:
    print (100 / y)
except ZeroDivisionError:
    print ("0 / error")
except:
    print ("bad")
#3. Create a variable that asks the user for a number. If the user input is not an integer, prints an exception for Value errors.
try:
    z = int(input())
    print ("good")
except ValueError:
    print("fail")
#4. Create a while loop that counts down from 5 to 0, but raises an exception when it counts below zero.
o = 5
while not o == 0:
    print (o)
    o -= 1
    if o == 0:
        raise Exception ("bad")