#samuel raymond
#5th
#senario

print("hello world")


dragons = {
    "white" : {
        "element" : "ice",
        "defence" : "c10",
        "offence" : "c15",
        "speed" : "c10"
    },
    "black": {
        "element": "acid",
        "defence": "c15",
        "offence": "c20",
        "speed": "c15"
    },
    "green": {
        "element": "poison",
        "defence": "c20",
        "offence": "c25",
        "speed": "c20"
    },
    "blue": {
        "element": "lighting",
        "defence": "c25",
        "offence": "c30",
        "speed": "c25"
    },
    "red": {
        "element": "fire",
        "defence": "c30",
        "offence": "c35",
        "speed": "c30"
    }
}


print ("red,blue,green,black,white")
print (dragons["red"]["offence"],dragons["blue"]["offence"],dragons["green"]["offence"],dragons["black"]["offence"],dragons["white"]["offence"],)



dragons["red"]["offence"] = input()
dragons["blue"]["offence"] = input()
dragons["green"]["offence"] = input()
dragons["black"]["offence"] = input()
dragons["white"]["offence"] = input()

print ("red,blue,green,black,white")
print (dragons["red"]["offence"],dragons["blue"]["offence"],dragons["green"]["offence"],dragons["black"]["offence"],dragons["white"]["offence"],)


















