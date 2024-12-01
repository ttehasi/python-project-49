from prompt import string


NUMBERS_OF_ATTEMPTS = 3


def samples(condition_answer, answ_and_qest, answ_and_qest2, answ_and_qest3):
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    number_of_successful_attempts = 0
    print(condition_answer)
    correct_answer, question = answ_and_qest
    for _ in range(NUMBERS_OF_ATTEMPTS):
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
        correct_answer, question = answ_and_qest3\
            if number_of_successful_attempts == 2 else answ_and_qest2
    if number_of_successful_attempts == NUMBERS_OF_ATTEMPTS:
        print(f'Congratulations, {name}!')
