#samuel raymond
#5th
#senario 2

print("hello world")


partyDictionary = {
    "LaeZel" : {
        "Race" : "Githyanki",
        "Class" : "Fighter",
        "Background" : "Soldier",
        "Health" : 12,
        "AC" : 17,
        "Damage" : 10,
    },
    "Shadowheart" : {
        "Race" : "Half-Elf",
        "Class" : "Cleric",
        "Background" : "Acolyte",
        "Health" : 10,
        "AC" : 14,
        "Damage" : 5,
    },
    "Gale" : {
        "Race" : "Human",
        "Class" : "Wizard",
        "Background" : "Sage",
        "Health" : 8,
        "AC" : 14,
        "Damage" : 17,
    },
    "Astarion" : {
        "Race" : "High Elf",
        "Class" : "Rogue",
        "Background" : "Charlatan",
        "Health" : 10,
        "AC" : 14,
        "Damage" : 12,
     },
    "white dragon": {
     "Race": "dragon",
     "Class": "wizerd",
     "Background": "tiamot",
     "Health": 100,
     "AC": 25,
     "Damage": 20,
    }
}
enmyDict = {
"white dragon": {
    "Race": "dragon",
    "Class": "wizerd",
    "Background": "tiamot",
    "Health": 100,
    "AC": 25,
    "Damage": 20,
}
}





print (enmyDict["white dragon"]["Health"] - partyDictionary["LaeZel"]["Damage"])
print (enmyDict["white dragon"]["Health"] - partyDictionary["Shadowheart"]["Damage"])
print (enmyDict["white dragon"]["Health"] - partyDictionary["Gale"]["Damage"])
print (enmyDict["white dragon"]["Health"] - partyDictionary["Astarion"]["Damage"])
















