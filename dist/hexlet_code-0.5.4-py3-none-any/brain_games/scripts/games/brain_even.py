import brain_games.scripts.games.sample


def main():
    cond_answer = 'Answer "yes" if the number is even, otherwise answer "no".'
    print(brain_games.scripts.games.sample.samples('brain-even', cond_answer))


if __name__ == '__main__':
    main()
