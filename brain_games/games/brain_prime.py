from brain_games.sample import samples


CON_ANSWER = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def type_brain_prime(num):
    re = []
    for i in range(1, num + 1):
        if num % i == 0:
            re.append(i)
    corr_answer = 'yes' if len(re) == 2 else 'no'
    return (corr_answer,
            f'Question: {num}')


def main():
    samples('brain-prime', CON_ANSWER)


if __name__ == '__main__':
    main()
