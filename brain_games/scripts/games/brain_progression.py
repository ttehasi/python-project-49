from brain_games.scripts.games.sample import samples


def main():
    cond_answer = 'What number is missing in the progression?'
    print(samples('brain-progression', cond_answer))


if __name__ == '__main__':
    main()
