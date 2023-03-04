import random


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_task():
    question = random.randint(1, 100)
    a = random.randint(1, 100)
    if (a % question != 0) and (question > 1) and \
            ((a ** (question - 1) - 1) % question == 0):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
