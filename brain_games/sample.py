import prompt
import random
# import brain_games.scripts.games.brain_calc
# import brain_games.scripts.games.brain_even
# import brain_games.scripts.games.brain_gcd


NUMBERS_OF_ATTEMPTS = 3


def samples(type_game, condition_answer):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    number_of_successful_attempts = 0
    print(condition_answer)
    for _ in range(NUMBERS_OF_ATTEMPTS):
        first_number = random.randint(1, 50)
        second_number = random.randint(1, 50)
        match type_game:
            case 'brain-even':
                import brain_games.scripts.games.brain_even
                correct_answer, question = (
                    brain_games.scripts.games.
                    brain_even.type_brain_even(first_number))
            case 'brain-calc':
                import brain_games.scripts.games.brain_calc
                first_number = random.randint(1, 25)
                second_number = random.randint(1, 25)
                arithmetic_operation = random.choice(['+', '-', '*'])
                correct_answer, question = (
                    brain_games.scripts.games.
                    brain_calc.type_brain_calc(first_number, second_number,
                                               arithmetic_operation))
            case 'brain-gcd':
                import brain_games.scripts.games.brain_gcd
                correct_answer, question = (
                    brain_games.scripts.games.
                    brain_gcd.type_brain_gcd(first_number, second_number))
            case 'brain-progression':
                import brain_games.scripts.games.brain_progression
                correct_answer, question = (
                    brain_games.scripts.games.
                    brain_progression.type_brain_progression(first_number))
            case 'brain-prime':
                import brain_games.scripts.games.brain_prime
                correct_answer, question = (
                    brain_games.scripts.games.
                    brain_prime.type_brain_prime(first_number))
        print(question)
        answer = input('Your answer: ')
        if answer == str(correct_answer):
            number_of_successful_attempts += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was"
                  f" '{correct_answer}'\n"
                  f"Let's try again, {name}!")
            break
    if number_of_successful_attempts == NUMBERS_OF_ATTEMPTS:
        print(f'Congratulations, {name}!')
