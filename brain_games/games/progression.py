import random

DESCRIPTION = 'What number is missing in the progression?'
MIN_START = 1
MAX_START = 50
MIN_STEP = 1
MAX_STEP = 10
PROGRESSION_LENGTH = 10


def generate_round():
    start = random.randint(MIN_START, MAX_START)
    step = random.randint(MIN_STEP, MAX_STEP)
    
    # Generar la progresión
    progression = [str(start + i * step) for i in range(PROGRESSION_LENGTH)]
    
    hidden_index = random.randint(0, PROGRESSION_LENGTH - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = ".."
    
    question = " ".join(progression)
    return question, correct_answer