import brain_games.scripts.games.sample


def main():
    cond_answer = 'What number is missing in the progression?'
    print(brain_games.scripts.games.sample.samples('brain-progression', cond_answer))


if __name__ == '__main__':
    main()
