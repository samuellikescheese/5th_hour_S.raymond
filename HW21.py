#Name:samuel
#Class: 5th Hour
#Assignment: HW21


#1. Make a nested dictionary with three entries called "sport1", "sport2", and "sport3" containing
#the name a sport the school partakes in, the amount of players a typical team uses during gameplay
#(ex: Basketball has 5 players), and if the sport uses a ball or not (as a boolean).
nestdict = {"sport1" : {"game" : "mincraft","players" : 4 ,"ball" : False},"sport2" : {"game" : "art", "players" : 20, "ball" : True}, "sport3" : {"game" : "murder", "players" : 2, "ball" : True}}

#2. Create a def function that pulls the values from the dictionary as arguments, adds together the
#players of all three sports, and prints the sum
def add():
    print(nestdict["sport1"]["players"]+nestdict["sport2"]["players"]+nestdict["sport3"]["players"])
#3. Call the function with arguments here
add()