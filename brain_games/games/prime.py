import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    if n < 2:
        return False
    # Verificamos divisores hasta la raíz cuadrada del número
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_round():
    # Generamos un número aleatorio entre 1 y 100
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = "yes" if is_prime(number) else "no"

    return question, correct_answer