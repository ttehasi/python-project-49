import prompt
import random


NUMBERS_OF_ATTEMPTS = 3


def type_brain_even(first_number):
    corr_ans = 'yes' if first_number % 2 == 0 else 'no'
    print(f'Question: {first_number}')
    return corr_ans


def type_brain_calc(first_number, sec_number):
    arithmetic_operation = random.choice(['+', '-', '*'])
    if arithmetic_operation == '+':
        correct_answer = first_number + sec_number
    elif arithmetic_operation == '-':
        correct_answer = first_number - sec_number
    else:
        correct_answer = first_number * sec_number
    print(f'Question: {first_number} {arithmetic_operation} {sec_number}')
    return correct_answer


def type_brain_gcd(frs_num, sec_num):
    re = []
    max_num = max(frs_num, sec_num)
    for i in range(1, max_num):
        if frs_num % i == 0 and sec_num % i == 0:
            re.append(i)
    print(f'Question: {frs_num} {sec_num}')
    return max(re)


def samples(type_game, condition_answer):
    name = prompt.string('May I have your name? ')
    number_of_successful_attempts = 0
    print(condition_answer)
    for _ in range(NUMBERS_OF_ATTEMPTS):
        first_number = random.randint(1, 50)
        second_number = random.randint(1, 50)
        if type_game == 'brain-even':
            correct_answer = type_brain_even(first_number)
        elif type_game == 'brain-calc':
            first_number = random.randint(1, 25)
            second_number = random.randint(1, 25)
            correct_answer = type_brain_calc(first_number, second_number)
        else:
            correct_answer = type_brain_gcd(first_number, second_number)
        answer = input('Your answer: ')
        if answer == str(correct_answer):
            number_of_successful_attempts += 1
            print('Correct!')
        else:
            return f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'\nLet's try again, {name}!"
    if number_of_successful_attempts == NUMBERS_OF_ATTEMPTS:
        return f'Congratulations, {name}!'
