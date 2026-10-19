import random

DESCRIPTION = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 50


def generate_round():
    num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    operator = random.choice(['+', '-', '*'])
    
    question = f"{num1} {operator} {num2}"
    correct_answer = str(eval(f"{num1} {operator} {num2}"))

    return question, correct_answer