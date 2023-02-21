import random


TASK = 'What is the result of the expression?'


def game_task():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    operators = ['-', '+', '*']
    oper = random.choice(operators)
    question = f'{number_1} {oper} {number_2}'
    if oper == '-':
        correct_answer = str(number_1 - number_2)
    if oper == '+':
        correct_answer = str(number_1 + number_2)
    if oper == '*':
        correct_answer = str(number_1 * number_2)
    return question, correct_answer
