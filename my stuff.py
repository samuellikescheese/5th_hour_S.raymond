import random

print ("welcome to slime gate")
print ("type 1 to let through")
print ("type 2 to not")
print ("plant = +1, fire = -1, water = 0 but is see through, light does what the slime before does, night does the opposite")
earth = 0
light = 0
score = 0
time = 0
change = 0
while not time == 30 :
    ai = random.randint(1, 7)
    if ai == 1:
        print("plant slime")
    if ai == 2:
        print("fire slime")
    if ai == 3:
        print("water slime")
    if ai == 4:
        print("light slime")
    if ai == 5:
        print("night slime")
    if ai == 6:
        print("earth slime")
    if ai == 7:
        print("air slime")
    m = int(input(""))
    if ai == 1:
        light = 1
        time += 1
        if m == 1:
            if earth == 1:
                score += 2
                print ("+2")
            if earth == 2:
                print ("+0")
            else:
                score += 1
                print("+1")
            earth = 0
        if m == 2:
            print ("he did not pass")
    if ai == 2:
        light = 2
        time += 1
        if m == 1:
            if earth == 1:
                print ("+0")
            if earth == 2:
                score -= 2
                print ("-2")
            else:
                score -= 1
                print("-1")
            earth = 0
        if m == 2:
            print("he did not pass")
    if ai == 3:
        time += 1
        if m == 1:
            print ("+0")
        if m == 2:
            print("he did not pass")
    if ai == 4:
        time += 1
        if light == 1:
            light = 1
            if m == 1:
                score += 1
                print("+1")
            if m == 2:
                print("he did not pass")
        if light == 2:
            light = 2
            if m == 1:
                score -= 1
                print("-1")
            if m == 2:
                print("he did not pass")
        if not light == 1 and not light == 2 :
            if m == 1:
                print("+0")
            if m == 2:
                print("he did not pass")
    if ai == 5:
        time += 1
        if light == 1:
            light = 2
            if m == 1:
                score -= 1
                print("-1")
            if m == 2:
                print("he did not pass")
        elif light == 2:
            light = 1
            if m == 1:
                score += 1
                print("+1")
                pass
            if m == 2:
                print("he did not pass")
        if not light == 1 and not light == 2 :
            if m == 1:
                print("+0")
            if m == 2:
                print("he did not pass")
    if ai == 6:
        light = 1
        time += 1
        earth = 2
        if m == 1:
            score += 1
            print ("+1")
        if m == 2:
            print ("he did not pass")
    if ai == 7:
        light = 2
        time += 1
        earth = 1
        if m == 1:
            score -= 1
            print ("-1")
        if m == 2:
            print ("he did not pass")
print (f"your score is {score}")





































































































































