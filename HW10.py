#samuel raymond
#5th
#HW6
import time
print ("Hello world")

#1. Create a while loop with variable i that counts down from 5 to 0
#and then prints "Hello World!" at the end.
i = 5
while i > 0 :
    time.sleep(0.4)
    print (i)
    i -= 1
else:
    time.sleep(0.4)
    print ("Hello world")
#2. Create a while loop that prints only even numbers
#between 1 and 30.
x = 2
while x <= 30:
    print (x)
    x += 2
else:
    print ("done")
#3. Create a while loop that repeats until the user
#inputs the number 0.
y = int(input ())
if y == 0:
    print ("thank you")
else :
    print ("press 0 then enter")
    while not y == 0:
        y = int(input ())
        print("press 0 then enter")
    else:
        print ("thank you")













