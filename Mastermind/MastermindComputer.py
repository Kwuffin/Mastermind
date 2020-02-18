antwoord = []
for i in range(0, 4):
    antwoordIn = input("Geef vier kleuren (getallen 1-6).")
    antwoordIn = int(antwoordIn)
    antwoord.append(antwoordIn)
print(antwoord, "Secret")


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
        guesses += 1
        return [3, 3, 4, 4]
    else:
        guesses += 1
        return mogelijkheden[0]




def feedback(): #Works
    fb = [0, 0, 0, 0] # '0' = geen kleuren / '1' = witte pin (juiste kleur, verkeerde plek) / '2' = zwarte pin (juiste kleur, juiste plek)
    if guess(mogelijkheden()) == antwoord:
        print("Geraden")
    else:
        counter = 0
        for i in guess(mogelijkheden()):
            counter += 1
            if i in antwoord and counter == 1:
                if antwoord[0] == i:
                    fb[0] = 2
                else:
                    fb[0] = 1
            elif i in antwoord and counter == 2:
                if antwoord[1] == i:
                    fb[1] = 2
                else:
                    fb[1] = 1
            elif i in antwoord and counter == 3:
                if antwoord[2] == i:
                    fb[2] = 2
                else:
                    fb[2] = 1
            elif i in antwoord and counter == 4:
                if antwoord[3] == i:
                    fb[3] = 2
                else:
                    fb[3] = 1
    return fb



mogelijkheden()
print(guess(mogelijkheden()), "Current guess")
print(feedback(), "0 = No pins / 1 = Correct colour, wrong place / 2 = Correct colour, correct place / Feedback")
