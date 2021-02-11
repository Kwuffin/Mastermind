from feedback import evaluate


def user_guess(ans):
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
