import brain_games.scripts.games.sample


def game_parity_check():
    cond_answer = 'Answer "yes" if the number is even, otherwise answer "no".'
    return brain_games.scripts.games.sample.samples('brain-even', cond_answer)


def main():
    print('Welcome to the Brain Games!')
    print(game_parity_check())


if __name__ == '__main__':
    main()
