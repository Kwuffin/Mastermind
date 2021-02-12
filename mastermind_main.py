import numpy as np
from simple_alg import simple_algorithm
from bongo_alg import bogo_algorithm
from user_play import user_guess
from knuth import knuth_algorithm


def comp_user_choice():
    """
    Asks the user if the computer or user guesses.

    :return: String "j" or "n"
    """

    userIn = False  # User Input is valid
    while not userIn:
        user_computer = input("Wil je de computer laten raden? (J/N)\n> ")
        if user_computer.lower() == "j" or user_computer.lower() == "n":
            userIn = True
        else:
            print("Ongeldige invoer, typ 'J' of 'N'")

    return user_computer


def main():
    user_input = comp_user_choice()

    # If user wants to guess
    if user_input == "n":
        answer = list(np.random.randint(1, 6, size=4))
        user_guess(answer)

    # If computer wants to guess
    else:
        alg_choice_valid = False  # User input is valid
        while not alg_choice_valid:
            try:
                algorithm_choice = int(input("Welk algoritme wil je gebruiken?\n"
                                             "1. Simple algorithm\n"
                                             "2. Bogo algorithm\n"
                                             "3. Worst-Case\n"
                                             "4. Exit\n"
                                             "> "))

                if 1 <= algorithm_choice < 4:
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

        # Selected simple algorithm
        if algorithm_choice == 1:
            simple_algorithm(answer)

        # Selected bogo algorithm
        elif algorithm_choice == 2:
            bogo_algorithm(answer)

        elif algorithm_choice == 3:
            knuth_algorithm(answer)

        # Exit
        elif algorithm_choice == 4:
            print("Tot de volgende keer!")
            exit()


if __name__ == '__main__':
    main()
