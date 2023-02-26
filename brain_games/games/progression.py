import random


TASK = 'What number is missing in the progression?'


def game_task():
    number_1 = random.randint(1, 20)
    number_2 = random.randint(80, 100)
    n = random.randint(2, 7)
    numbers = range(number_1, number_2, n)
    progression = []
    for i in numbers:
        progression.append(str(i))
    progression = progression[1: 11]
    correct_answer = progression[random.randint(1, 9)]
    progression = " ".join(progression)
    for i in progression:
        progression = progression.replace(correct_answer, '..')
    question = f'{progression}'
    return question, correct_answer
