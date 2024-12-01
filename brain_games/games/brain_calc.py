from brain_games.sample import gen_rand_num
from brain_games.sample import samples


CON_ANSWER = 'What is the result of the expression?'


def type_brain_calc(numbers):
    correct_answer = ''
    first_number, sec_number, arithmetic_operation = numbers
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
    samples(CON_ANSWER, type_brain_calc(gen_rand_num()),
            type_brain_calc(gen_rand_num()), type_brain_calc(gen_rand_num()))


if __name__ == '__main__':
    main()
