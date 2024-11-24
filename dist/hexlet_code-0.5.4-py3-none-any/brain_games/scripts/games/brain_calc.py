import brain_games.scripts.games.sample


def main():
    cond_answer = 'What is the result of the expression?'
    print(brain_games.scripts.games.sample.samples('brain-calc', cond_answer))


if __name__ == '__main__':
    main()
