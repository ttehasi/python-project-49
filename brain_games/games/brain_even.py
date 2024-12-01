import random
from brain_games.sample import samples


CON_ANSWER = 'Answer "yes" if the number is even, otherwise answer "no".'


def type_brain_even():
    first_number = random.randint(1, 50)
    corr_ans = 'yes' if first_number % 2 == 0 else 'no'
    return (corr_ans,
            f'Question: {first_number}')


def main():
    samples(CON_ANSWER, type_brain_even(),
            type_brain_even(), type_brain_even())


if __name__ == '__main__':
    main()
