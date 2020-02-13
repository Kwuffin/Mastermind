import random

antwoord = []
for i in range(0, 4):
    antwoordIn = input("Geef vier kleuren (getallen 1-6).")
    antwoordIn = int(antwoordIn)
    antwoord.append(antwoordIn)
print(antwoord)


def mogelijkheden(): #works
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


def guess():


#def feedback():

print(mogelijkheden())