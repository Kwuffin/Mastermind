def mogelijkheden():
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


def guess(mogelijkheden):
    guesses = 0
    if guesses == 0:
        guesses += 1
        return [3, 3, 4, 4]
    else:
        guesses += 1
        return mogelijkheden[0]


def feedback(guess):
    fb = [0, 0, 0, 0] # '0' = geen kleuren / '1' = witte pin (juiste kleur, verkeerde plek) / '2' = zwarte pin (juiste kleur, juiste plek)
    if guess == antwoord:
        print("De computer heeft de secret geraden!")
    else:
        for i in guess:
            for j in range(0,4):
                if i in antwoord:
                    if antwoord[j] == i:
                        fb[j] = 2
                    else:
                        fb[j] = 1
    return fb


antwoord = []
print("-------------------------   --= < ( M A S T E R M I N D ) > =--   -------------------------")
for i in range(0, 4):
    antwoordIn = input("Geef een kleur (getallen 1-6): ")
    antwoordIn = int(antwoordIn)
    antwoord.append(antwoordIn)
print("-------------------------------------------------------------------------------------------\n", antwoord, "is je secret\n-------------------------------------------------------------------------------------------")


mogelijkheden()
print(guess(mogelijkheden()), "computergok.")
print(feedback(guess(mogelijkheden())), "0 = Geen pins / 1 = Juiste kleur op de verkeerde plaats / 2 = Juiste kleur op de juiste plek / Feedback")
