import random

antwoord = []
for i in range(0, 4):
    a = random.randint(1,6)
    antwoord.append(a)
    print(antwoord)

def userInput():
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
        print("----------------------")


    if userInput == antwoord:
        print("Je hebt het geraden!")
        return True
    return False

while userInput() == False:
    userInput()