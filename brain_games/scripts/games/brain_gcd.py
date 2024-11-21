import brain_games.scripts.games.sample


def game_gcd():
    cond_answer = 'Find the greatest common divisor of given numbers.'
    return brain_games.scripts.games.sample.samples('brain-gcd', cond_answer)


def main():
    print('Welcome to the Brain Games!')
    print(game_gcd())


if __name__ == '__main__':
    main()
