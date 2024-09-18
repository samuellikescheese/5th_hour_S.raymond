#samuel raymond
#5th
#senario

print("hello world")


dragons = {
    "white" : {
        "element" : "ice",
        "defence" : 10,
        "offence" : 15,
        "speed" : 10
    },
    "black": {
        "element": "acid",
        "defence": 15,
        "offence": 20,
        "speed":15
    },
    "green": {
        "element": "poison",
        "defence": 20,
        "offence": 25,
        "speed": 20
    },
    "blue": {
        "element": "lighting",
        "defence": 25,
        "offence": 30,
        "speed": 25
    },
    "red": {
        "element": "fire",
        "defence": 30,
        "offence": 35,
        "speed": 30
    }
}


print ("red,blue,green,black,white")
print (dragons["red"]["offence"],dragons["blue"]["offence"],dragons["green"]["offence"],dragons["black"]["offence"],dragons["white"]["offence"],)



dragons["red"]["offence"] = int(input("new R"))
dragons["blue"]["offence"] = int(input("new Bu"))
dragons["green"]["offence"] = int(input("new G"))
dragons["black"]["offence"] = int(input("new Ba"))
dragons["white"]["offence"] = int(input("new W"))

print ("red,blue,green,black,white")
print (dragons["red"]["offence"],dragons["blue"]["offence"],dragons["green"]["offence"],dragons["black"]["offence"],dragons["white"]["offence"],)


















