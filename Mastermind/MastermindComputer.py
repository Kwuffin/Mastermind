antwoord = []
antwoord = input("Geef vier kleuren (getallen 1-6).").split()
print(antwoord)


def mogelijkheden(): #finished
    combination_list = []
    colors = ['1', '2', '3', '4', '5', '6']
    for c1 in colors:
        for c2 in colors:
            for c3 in colors:
                for c4 in colors:
                    combination_list.append([c1, c2, c3, c4])
    return combination_list


def guess(mogelijkheden): #In progress
    guesses = 0
    if guesses == 0:
        return mogelijkheden[0]
    else:
        return mogelijkheden[0] #Uhhh... ?????


def feedback(): #Needs to be worked on / In progress
    fb = [0, 0] # '0' = geen kleuren / '1' = witte pin (juiste kleur, verkeerde plek) / '2' = zwarte pin (juiste kleur, juiste plek)
    if guess(mogelijkheden()) == antwoord:
        print("Geraden")
    else:
        for i in guess(mogelijkheden()):
            if i in antwoord:
                for j in antwoord:
                    if i == j:
                        fb.append(2)
                        break
                    else:
                        fb.append(1)
                        break
    return fb


print(mogelijkheden())
print(guess(mogelijkheden()))
print(feedback())
