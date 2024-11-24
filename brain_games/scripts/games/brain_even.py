from brain_games.scripts.games.sample import samples


def main():
    cond_answer = 'Answer "yes" if the number is even, otherwise answer "no".'
    print(samples('brain-even', cond_answer))


if __name__ == '__main__':
    main()
