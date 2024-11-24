from brain_games.scripts.games.sample import samples


def main():
    cond_answer = 'What is the result of the expression?'
    print(samples('brain-calc', cond_answer))


if __name__ == '__main__':
    main()
