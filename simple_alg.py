from feedback import evaluate
from random import choice


def simple_algorithm(answer):
    """
    Simple algorithm uit de 'YET ANOTHER MASTERMIND STRATEGY' van de Universiteit Groningen.

    :param answer: Secret code
    """
    possibilities = []

    # Creates all possible answers in order [1, 1, 1, 1] ... [6, 6, 6, 6]
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                for m in range(1, 7):
                    possibilities.append([i, j, k, m])

    correct = False

    count = 0
    while not correct:
        # Guesses the first possible guess in the sorted list of possibilities
        guess = possibilities[0]
        count += 1  # Counts amount of guesses

        print(f"Compuer gokt: {guess}")

        # Feedback
        black, white = evaluate(answer, guess)

        # If all pins are in the correct place:
        if black == 4:
            correct = True

        # Eliminates possibilities
        new_pos = []
        for possibility in possibilities:
            if evaluate(possibility, guess) == (black, white):
                new_pos.append(possibility)

        possibilities = new_pos

    print(f"De computer heeft de secret gegokt in {count} gokken!")
