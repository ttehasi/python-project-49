import prompt

NUMBERS_OF_ATTEMPTS = 3


def samples(condition_answer, answ_and_qest):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    number_of_successful_attempts = 0
    print(condition_answer)

    for _ in range(NUMBERS_OF_ATTEMPTS):
        correct_answer, question = answ_and_qest()
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
