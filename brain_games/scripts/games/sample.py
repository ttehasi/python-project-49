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


def typo_brain_progression(first_num):
    re = []
    range_progressing = random.randint(5, 10)
    sec_num = random.randint(1, 5)
    for _ in range(range_progressing):
        re.append(str(first_num))
        first_num += sec_num
    index_replace_num = re.index(random.choice(re[1:]))
    replace_num = re[index_replace_num - 1]
    re.insert(index_replace_num, '..')
    re.remove(re[index_replace_num - 1])
    progressing_str = ' '.join(re)
    print(f'Question: {progressing_str}')
    return replace_num


def typo_brain_prime(num):
    re = []
    for i in range(1, num + 1):
        if num % i == 0:
            re.append(i)
    print(f'Question: {num}')
    return 'yes' if len(re) == 2 else 'no'


def samples(type_game, condition_answer):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    number_of_successful_attempts = 0
    print(condition_answer)
    correct_answer = ''
    for _ in range(NUMBERS_OF_ATTEMPTS):
        first_number = random.randint(1, 50)
        second_number = random.randint(1, 50)
        match type_game:
            case 'brain-even':
                correct_answer = type_brain_even(first_number)
            case 'brain-calc':
                first_number = random.randint(1, 25)
                second_number = random.randint(1, 25)
                correct_answer = type_brain_calc(first_number, second_number)
            case 'brain-gcd':
                correct_answer = type_brain_gcd(first_number, second_number)
            case 'brain-progression':
                correct_answer = typo_brain_progression(first_number)
            case 'brain-prime':
                correct_answer = typo_brain_prime(first_number)
        answer = input('Your answer: ')
        if answer == str(correct_answer):
            number_of_successful_attempts += 1
            print('Correct!')
        else:
            return f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'\nLet's try again, {name}!"
    if number_of_successful_attempts == NUMBERS_OF_ATTEMPTS:
        return f'Congratulations, {name}!'
