import random

from brain_games.sample import samples

CON_ANSWER = 'What is the result of the expression?'


def type_brain_calc():
    correct_answer = ''
    first_number = random.randint(1, 25)
    sec_number = random.randint(1, 25)
    arithmetic_operation = random.choice(['-', '+', '*'])
    match arithmetic_operation:
        case '+':
            correct_answer = first_number + sec_number
        case '-':
            correct_answer = first_number - sec_number
        case '*':
            correct_answer = first_number * sec_number
    return (correct_answer,
            f'Question: {first_number} {arithmetic_operation} {sec_number}')


def main():
    samples(CON_ANSWER, type_brain_calc)


if __name__ == '__main__':
    main()
