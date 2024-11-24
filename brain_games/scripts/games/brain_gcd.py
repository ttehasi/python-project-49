from brain_games.scripts.games.sample import samples


def main():
    cond_answer = 'Find the greatest common divisor of given numbers.'
    print(samples('brain-gcd', cond_answer))


if __name__ == '__main__':
    main()
