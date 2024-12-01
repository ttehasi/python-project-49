from brain_games.sample import gen_rand_num
from brain_games.sample import samples


CON_ANSWER = 'Find the greatest common divisor of given numbers.'


def type_brain_gcd(numbers):
    frs_num, sec_num, arithmetic_operation = numbers
    re = []
    max_num = max(frs_num, sec_num)
    for i in range(1, max_num + 1):
        if frs_num % i == 0 and sec_num % i == 0:
            re.append(i)
    return (max(re),
            f'Question: {frs_num} {sec_num}')


def main():
    samples(CON_ANSWER, type_brain_gcd(gen_rand_num()),
            type_brain_gcd(gen_rand_num()), type_brain_gcd(gen_rand_num()))


if __name__ == '__main__':
    main()
