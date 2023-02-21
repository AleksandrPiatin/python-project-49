import prompt


def play_game(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.TASK)
    winstrike = 0
    while winstrike < 3:
        question, correct_answer = game.game_task()
        if play_round(question, correct_answer):
            winstrike += 1
        else:
            return print(f"Let's try again, {name}!")
    print(f"Congratulations, {name}!")


def play_round(question, correct_answer):
    print(f'Question: {question}')
    user_answer = prompt.string('Your answer: ')
    if user_answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(f"'{user_answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.")
        return False
