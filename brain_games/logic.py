import random
import prompt


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def greet():
    print("Welcome to the Brain Games!")
    welcome_user()


def even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
        number = random.randint(1, 100)
        print(f'Question: {number}')
        user_answer = prompt.string('Your answer? ')
        answer_yes = 'yes'
        answer_no = 'no'
        if (number % 2 == 0 and user_answer.lower() == answer_yes) or \
                (number % 2 == 1 and user_answer.lower() == answer_no):
            print('Correct!')
            count += 1
        else:
            if number % 2 == 0 and user_answer.lower() != answer_yes:
                return print(f"'{user_answer}' is wrong answer ;(. \
Correct answer was '{answer_yes}'.\nLet's try again, {name}!")
            if number % 2 == 1 and user_answer.lower() != answer_no:
                return print(f"'{user_answer}' is wrong answer ;(. \
Correct answer was '{answer_no}'.\nLet's try again, {name}!")
    print(f"Congratulations, {name}!")
