import random

import prompt

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def run_even_game():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(3):
        number = random.randint(1, 50)
        print(f"Question: {number}")
        answer = prompt.string("Your answer: ")

        correct_answer = "yes" if number % 2 == 0 else "no"

        if answer == correct_answer:
            print("Correct!")
        else:
            print(f"""'{answer}' is wrong answer ;(. 
                Correct answer was '{correct_answer}'.""")
            print(f"Let's try again, {name}!")
            return

        print(f"Congratulations, {name}!")
