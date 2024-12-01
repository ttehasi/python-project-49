from brain_games.sample import gen_rand_num
from brain_games.sample import samples


CON_ANSWER = 'Answer "yes" if the number is even, otherwise answer "no".'


def type_brain_even(numbers):
    first_number, sec_number, arithmetic_operation = numbers
    corr_ans = 'yes' if first_number % 2 == 0 else 'no'
    return (corr_ans,
            f'Question: {first_number}')


def main():
    samples(CON_ANSWER, type_brain_even(gen_rand_num()),
            type_brain_even(gen_rand_num()), type_brain_even(gen_rand_num()))


if __name__ == '__main__':
    main()
