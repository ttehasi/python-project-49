from brain_games.sample import samples


CON_ANSWER = 'Find the greatest common divisor of given numbers.'


def type_brain_gcd(frs_num, sec_num):
    re = []
    max_num = max(frs_num, sec_num)
    for i in range(1, max_num + 1):
        if frs_num % i == 0 and sec_num % i == 0:
            re.append(i)
    return (max(re),
            f'Question: {frs_num} {sec_num}')


def main():
    samples('brain-gcd', CON_ANSWER)


if __name__ == '__main__':
    main()
