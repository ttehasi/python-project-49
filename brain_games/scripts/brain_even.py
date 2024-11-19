import random
import prompt


NUMBERS_OF_ATTEMPTS = 3


def game_parity_check():
    name = prompt.string('May I have your name? ')
    number_of_successful_attempts = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(NUMBERS_OF_ATTEMPTS):
        random_nuber = random.randint(0, 100)
        parity = 'yes' if random_nuber % 2 == 0 else 'no'
        print(f'Question: {random_nuber}')
        answer = input('Your answer: ')
        if answer != parity:
            return f"'{answer}' is wrong answer ;(. Correct answer was '{parity}'\nLet's try again, Bill!"
        if answer == parity:
            number_of_successful_attempts += 1
            print('Correct!')
        if number_of_successful_attempts == NUMBERS_OF_ATTEMPTS:
            return f'Congratulations, {name}!'


def main():
    print('Welcome to the Brain Games!')
    print(game_parity_check())


if __name__ == '__main__':
    main()
