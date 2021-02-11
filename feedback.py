def black_feedback(answer, guess):
    black = 0

    count = 0
    for i in guess:
        if i == answer[count]:
            black += 1
        count += 1

    return black


def white_feedback(answer, guess):
    white = 0
    answer2 = answer.copy()

    for i in guess:
        if i in answer2:
            white += 1
            answer2.remove(i)

    return white


def evaluate(answer, user_ans):
    black_pins = black_feedback(answer, user_ans)
    white_pins = white_feedback(answer, user_ans)

    white_pins -= black_pins

    return black_pins, white_pins
