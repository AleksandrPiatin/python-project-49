import random


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_task():
    question = random.randint(2, 100)
    a = 2
    '''take the number "a" to check for simplicity'''
    if ((a ** (question - 1) - 1) % question == 0):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
