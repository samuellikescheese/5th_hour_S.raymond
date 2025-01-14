#Name:samuel raymond
#Class: 5th Hour
#Assignment: HW15

#1. Create a def function that prints out "Hello World!"
def hello_world():
    print ("hello world")


#2. Create a def function that calculates the average of three numbers.
def aver(z,x,y):
    r =z+x+y
    print(r/3)

#3. Create a def function with the names of 5 animals as arguments, treats it like a list, and
#prints the name of the third animal.
def ani(*cheese):
    print (cheese[2])

#4. Create a def function that loops from 1 to the number put in the argument.
def num(x):
    h = 0
    while not h == x:
        h += 1
        print(h)


#5. Call all of the functions created in 1 - 4 with relevant arguments.
hello_world()
aver(7,2,5)
ani("dog","cat","dude","car","tank")
num(int(input()))












