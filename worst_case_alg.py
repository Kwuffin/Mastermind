from feedback import evaluate


def worst_case_algorithm(answer):
    """
    From:
    Donald Knuth Algorithm Mastermind.
    (2020, June 17). Stack Overflow.
    https://stackoverflow.com/questions/62430071/donald-knuth-algorithm-mastermind#:%7E:text=Mastermind%2DFive%2DGuess%2DAlgorithm,the%20number%20of%20possible%20patterns.


    :param answer: Secret code
    """
    possibilities = []

    # Creates all possible answers in order [1, 1, 1, 1] ... [6, 6, 6, 6]
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                for m in range(1, 7):
                    possibilities.append([i, j, k, m])

    unused = possibilities.copy()

    correct = False
    count = 0
    while not correct:
        # Guesses the first possible guess in the sorted list of possibilities
        count += 1  # Counts amount of guesses

        if count == 1:
            black, white = 0, 0
            guess = [1, 1, 2, 2]  # Initial guess

        else:
            guess = minimax(possibilities, unused, black, white)

        print(f"Compuer gokt: {guess}")
        unused.remove(guess)

        # Feedback
        black, white = evaluate(answer, guess)

        # If all pins are in the correct place:
        if black == 4:
            correct = True

        # Eliminate possibilities
        new_pos = []
        for possibility in possibilities:
            if evaluate(possibility, guess) == (black, white):
                new_pos.append(possibility)

        possibilities = new_pos

    print(f"De computer heeft de secret gegokt in {count} gokken!")


def minimax(possibilities, unused, old_black, old_white):
    elim_dict = {}
    for code in unused:
        new_posibilities = []
        for possibility in possibilities:
            if evaluate(possibility, code) == (old_black, old_white):
                new_posibilities.append(possibility)

        elim_dict[tuple(code)] = len(possibilities) - len(new_posibilities)

    return list(max(elim_dict, key=elim_dict.get))
