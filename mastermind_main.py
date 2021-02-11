import numpy as np
from simple_alg import simple_algorithm
from bongo_alg import bongo_algorithm
from feedback import evaluate


def user_guess(ans):
    print(ans)
    # Counts amount of guesses
    count = 0

    correct = False
    while not correct:
        guess = []
        count += 1

        for _ in range(4):
            valid = False  # True if the given number is between 1 and 6

            while not valid:
                try:
                    guess_num = int(input("Geef een getal\n> "))

                    if 1 <= guess_num <= 6:
                        valid = True

                    else:
                        print("Ongeldig getal, voer een getal in van 1 tot 6")

                except ValueError:
                    print("Geen geldige invoer, voer een getal in (0-6)")

            guess.append(guess_num)

        print(f"\nJouw gok: {guess}")

        black, white = evaluate(ans, guess)

        print(f"Feedback:\n"
              f"{black} zwarte pin(s)\n"
              f"{white} witte pin(s)\n")

        if black == 4:
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

    # If user wants to guess
    if user_input == "n":
        answer = list(np.random.randint(1, 6, size=4))
        user_guess(answer)

    # If computer wants to guess
    else:
        alg_choice_valid = False
        while not alg_choice_valid:
            try:
                algorithm_choice = int(input("Welk algoritme wil je gebruiken?\n"
                                             "1. Simple algorithm\n"
                                             "2. Bongo algorithm\n"
                                             "> "))

                if 1 <= algorithm_choice < 3:
                    alg_choice_valid = True

                else:
                    print("Voer een geldig getal in")

            except ValueError:
                print("Voer een getal in.")

        answer = []
        for _ in range(4):
            valid = False  # True if the given number is between 1 and 6

            while not valid:
                try:
                    answer_num = int(input("Geef een getal\n> "))

                    if 1 <= answer_num <= 6:
                        valid = True

                    else:
                        print("Ongeldig getal, voer een getal in van 1 tot 6")

                except ValueError:
                    print("Geen geldige invoer, voer een getal in (0-6)")

            answer.append(answer_num)

        print(f"Je secret: {answer}")

        if algorithm_choice == 1:
            simple_algorithm(answer)

        elif algorithm_choice == 2:
            bongo_algorithm(answer)


if __name__ == '__main__':
    main()
