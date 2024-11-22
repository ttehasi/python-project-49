import brain_games.scripts.games.sample


def game_progression():
    cond_answer = 'What number is missing in the progression?'
    return brain_games.scripts.games.sample.samples('brain-progression', cond_answer)


def main():
    print(game_progression())


if __name__ == '__main__':
    main()
