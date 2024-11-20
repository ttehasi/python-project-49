import prompt
import random


NUMBERS_OF_ATTEMPTS = 3


def samples(type_game, condition_answer):
    name = prompt.string('May I have your name? ')
    number_of_successful_attempts = 0
    print(condition_answer)
    for _ in range(NUMBERS_OF_ATTEMPTS):
        first_number = random.randint(0, 25)
        second_number = random.randint(0, 25)
        if type_game == 'brain-even':
            correct_answer = 'yes' if first_number % 2 == 0 else 'no'
            print(f'Question: {first_number}')
        else:
            arithmetic_operation = random.choice(['+', '-', '*'])
            if arithmetic_operation == '+':
                correct_answer = first_number + second_number
            elif arithmetic_operation == '-':
                correct_answer = first_number - second_number
            else:
                correct_answer = first_number * second_number
            print(f'Question: {first_number} {arithmetic_operation} {second_number}')
        answer = input('Your answer: ')
        if answer != str(correct_answer):
            return f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'\nLet's try again, {name}!"
        if answer == str(correct_answer):
            number_of_successful_attempts += 1
            print('Correct!')
    if number_of_successful_attempts == NUMBERS_OF_ATTEMPTS:
        return f'Congratulations, {name}!'
