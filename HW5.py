#samuel raymond
#5th
#HW5

print("hello world")

x = int(input ())
y = int(input ())
z = int(input ())


cheese = (x, y, z)
print (cheese)
if  x > y and x > z :
    print (f"{x}is the highest")
if  y > x and y > z :
    print (f"{y}is the highest")
if  z > y and z > x :
    print (f"{z}is the highest")
if  z == y and z == x and x == y :
    print ("all is even")
if  z < y  and x == y :
    print (f"{x} and {y} are highest ")
if  z > y and z == x:
    print (f"{z} and {x} are highest")
if  z == y and z > x :
    print (f"{z} and {y} are highest")

else : print ("error that is not a number")












