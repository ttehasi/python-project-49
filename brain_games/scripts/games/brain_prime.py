import brain_games.scripts.games.sample


def main():
    cond_answer = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    print(brain_games.scripts.games.sample.samples('brain-prime', cond_answer))


if __name__ == '__main__':
    main()
