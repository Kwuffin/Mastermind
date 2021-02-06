import numpy as np


def evaluate(answer, user_ans):
    feedback = []
    count = 0

    for i in user_ans:

        if i == answer[count]:
            feedback.append(2)

        elif i in answer:
            feedback.append(1)

        else:
            feedback.append(0)

        count += 1
    return feedback


def user_guess():
    answer = np.random.randint(1, 6, size=4)
    print(answer)

    count = 0

    correct = False
    while not correct:
        user_ans = []
        count += 1

        for _ in range(4):
            valid = False

            while not valid:
                try:
                    guess_num = int(input("Geef een getal\n> "))

                    if 1 <= guess_num <= 6:
                        valid = True

                    else:
                        print("Ongeldig getal, voer een getal in van 1 tot 6")

                except ValueError:
                    print("Geen geldige invoer, voer een getal in (0-6)")

            user_ans.append(guess_num)

        print(f"Jouw gok: {user_ans}")

        feedback = evaluate(answer, user_ans)

        print(f"Feedback: {feedback}")

        if feedback == [2, 2, 2, 2]:
            correct = True

    if count > 1:
        print(f"Gefeliciteerd! Je hebt de code geraden in {count} gokken!")
    else:
        print(f"Gefeliciteerd! Je hebt de code geraden in één gok!")


def menu():
    userIn = False
    while not userIn:
        user_computer = input("Wil je de computer laten raden? (J/N)\n> ")
        if user_computer.lower() == "j" or user_computer.lower() == "n":
            userIn = True
        else:
            print("Ongeldige invoer, typ 'J' of 'N'")

    return user_computer


def main():
    user_input = menu()
    if user_input == "n":
        user_guess()


if __name__ == '__main__':
    main()
