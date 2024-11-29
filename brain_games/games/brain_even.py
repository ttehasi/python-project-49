import brain_games.sample


CON_ANSWER = 'Answer "yes" if the number is even, otherwise answer "no".'


def type_brain_even(first_number):
    corr_ans = 'yes' if first_number % 2 == 0 else 'no'
    return (corr_ans,
            f'Question: {first_number}')


def main():
    brain_games.sample.samples('brain-even', CON_ANSWER)


if __name__ == '__main__':
    main()
