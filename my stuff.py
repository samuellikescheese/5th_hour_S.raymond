import random

print ("press 1 to play slime gate")
light = 0
score = 0
time = 0
change = 0
while not time == 20 :
    ai = random.randint(1, 5)
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
    m = int(input(""))
    if ai == 1:
        light = 1
        time += 1
        if m == 1:
            score += 1
            print ("+1")
        if m == 2:
            print ("he did not pass")
    if ai == 2:
        light = 2
        time += 1
        if m == 1:
            score -= 1
            print("-1")
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
print (score)





































































































































