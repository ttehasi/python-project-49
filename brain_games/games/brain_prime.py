from brain_games.sample import gen_rand_num
from brain_games.sample import samples


CON_ANSWER = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def type_brain_prime(numbers):
    num, sec_number, arithmetic_operation = numbers
    re = []
    for i in range(1, num + 1):
        if num % i == 0:
            re.append(i)
    corr_answer = 'yes' if len(re) == 2 else 'no'
    return (corr_answer,
            f'Question: {num}')


def main():
    samples(CON_ANSWER, type_brain_prime(gen_rand_num()),
            type_brain_prime(gen_rand_num()), type_brain_prime(gen_rand_num()))


if __name__ == '__main__':
    main()
