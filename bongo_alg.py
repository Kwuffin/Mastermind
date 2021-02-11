from feedback import evaluate
from itertools import permutations
from random import choice


def bogo_algorithm(answer):
    """
    Gebaseerd op het bogo-sorteer algoritme
    met het tijdscomplexiteit van O(n!)

    Het originele bogo algoritme blijft willekeurig willekeurig gokken
    totdat de uitkomst goed is. Dit algoritme wordt ook wel random sort genoemd.

    :param answer: Secret code
    """
    possibilities = list(permutations([1, 2, 3, 4, 5, 6], 4))

    correct = False

    count = 0
    while not correct:
        # Guesses a random guess
        guess = choice(possibilities)

        count += 1

        print(f"Compuer gokt: {guess}")

        black, white = evaluate(answer, guess)

        # If all pins are in the correct place:
        if black == 4:
            correct = True

    print(f"De computer heeft de secret gegokt in {count} gokken... (lol)")


