from random import randint, choice
from brain_games.sample import samples


CON_ANSWER = 'What number is missing in the progression?'


def type_brain_progression():
    first_num = randint(1, 50)
    re = []
    range_progressing = randint(5, 10)
    sec_num = randint(1, 5)
    for _ in range(range_progressing):
        re.append(str(first_num))
        first_num += sec_num
    index_replace_num = re.index(choice(re[1:]))
    replace_num = re[index_replace_num - 1]
    re.insert(index_replace_num, '..')
    re.remove(re[index_replace_num - 1])
    progressing_str = ' '.join(re)
    return (replace_num,
            f'Question: {progressing_str}')


def main():
    samples(CON_ANSWER, type_brain_progression(),
            type_brain_progression(), type_brain_progression())


if __name__ == '__main__':
    main()
