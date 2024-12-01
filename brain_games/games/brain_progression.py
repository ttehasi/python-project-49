from random import randint, choice
import brain_games.sample


CON_ANSWER = 'What number is missing in the progression?'


def type_brain_progress():
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
    brain_games.sample.samples(CON_ANSWER, type_brain_progress(),
                               type_brain_progress(), type_brain_progress())


if __name__ == '__main__':
    main()
