from brain_games.sample import samples
import random


CON_ANSWER = 'What number is missing in the progression?'


def type_brain_progression(first_num):
    re = []
    range_progressing = random.randint(5, 10)
    sec_num = random.randint(1, 5)
    for _ in range(range_progressing):
        re.append(str(first_num))
        first_num += sec_num
    index_replace_num = re.index(random.choice(re[1:]))
    replace_num = re[index_replace_num - 1]
    re.insert(index_replace_num, '..')
    re.remove(re[index_replace_num - 1])
    progressing_str = ' '.join(re)
    return (replace_num,
            f'Question: {progressing_str}')


def main():
    samples('brain-progression', CON_ANSWER)


if __name__ == '__main__':
    main()
