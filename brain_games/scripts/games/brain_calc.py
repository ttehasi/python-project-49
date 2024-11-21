import brain_games.scripts.games.sample


def calc_game():
    cond_answer = 'What is the result of the expression?'
    return brain_games.scripts.games.sample.samples('brain-calc', cond_answer)


def main():
    print('Welcome to the Brain Games!')
    print(calc_game())


if __name__ == '__main__':
    main()
