from feedback import evaluate
from random import choice


def simple_algorithm(answer):
    possibilities = []

    # Creates all possible answers in order [1, 1, 1, 1] ... [6, 6, 6, 6]
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                for l in range(1, 7):
                    possibilities.append([i, j, k, l])

    correct = False

    count = 0
    while not correct:
        # Guesses the first possible guess in the sorted list of possibilities
        guess = possibilities[0]

        count += 1

        print(f"Compuer gokt: {guess}")

        black, white = evaluate(answer, guess)

        # If all pins are in the correct place:
        if black == 4:
            correct = True

        result = []
        for possibility in possibilities:
            if evaluate(possibility, guess) == (black, white):
                result.append(possibility)

        possibilities = result

    print(f"De computer heeft de secret gegokt in {count} gokken!")
