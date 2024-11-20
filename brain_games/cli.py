import prompt


def get_username():
    name = prompt.string('May I have your name? ')
    return name


def welcome_user():
    return f'Hello, {get_username()}!'
