import brain_games.sample


CON_ANSWER = 'What is the result of the expression?'


def type_brain_calc(first_number, sec_number, arithmetic_operation):
    correct_answer = ''
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
    brain_games.sample.samples('brain-calc', CON_ANSWER)


if __name__ == '__main__':
    main()
