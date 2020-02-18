antwoord = []
for i in range(0, 4):
    antwoordIn = input("Geef vier kleuren (getallen 1-6).")
    antwoordIn = int(antwoordIn)
    antwoord.append(antwoordIn)
print(antwoord)


def mogelijkheden(): #finished
    mList = []
    list = [0, 0, 0, 0]
    for i in range(0, 6):
        list[0] += 1
        for i2 in range(0,6):
            list[1] += 1
            if list[1] == 7:
                list[1] = 1
            for i3 in range(0,6):
                list[2] += 1
                if list[2] == 7:
                    list[2] = 1
                for i4 in range(0, 6):
                    list[3] += 1
                    if list[3] == 7:
                        list[3] = 1
                    mList.append(list[:])
    return mList


def guess(mogelijkheden): #In progress
    guesses = 0
    if guesses == 0:
        return mogelijkheden[0]
    else:
        return mogelijkheden[0] #Uhhh... ?????



def feedback(): #Needs to be worked on / In progress
    fb = [] # '0' = geen kleuren / '1' = witte pin (juiste kleur, verkeerde plek) / '2' = zwarte pin (juiste kleur, juiste plek)
    if guess(mogelijkheden()) == antwoord:
        print("Geraden")
    else:
        for i in guess(mogelijkheden()):
            if i in antwoord:
                fb.append(1)
                for j in antwoord:
                    if i == j:
                        fb.append(2)
            else:
                fb.append(0)
    return fb

def listremove():




print(mogelijkheden())
print(guess(mogelijkheden()))
print(feedback())
