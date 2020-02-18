import random

antwoord = []
for i in range(0, 4):
    a = random.randint(1,6)
    antwoord.append(a)
    print(antwoord)


def feedback():
    counter == 0
    j = userInput[counter]
    for i in antwoord:

            p = antwoord.index(i)
            p2 = userInput.index(j)
            if p == p2:
                print("II")
            elif p != p2 and j == i:
                print("I")
            else:
                print("O")


while True:
    userInput = []
    counter = 0
    for i in range(0, 4):
        try:
            a = input("Input:   ")
        except ValueError:
            print("Geef getallen.")
            break
        a = int(a)
        userInput.append(a)
        counter += 1

    if counter == 4:
        feedback()
        print("----------------------")

    if userInput == antwoord:
        print("Je hebt het geraden!")
        break