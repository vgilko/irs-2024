import razdel
from pymystem3 import Mystem


def read_data(file_name: str) -> str:
    with open(file_name, 'r') as file:
        return ''.join(file.readlines())


def dump_data(file_name: str, data: [str]):
    with open(file_name, 'w') as file:
        for value in data:
            file.write(value + '\n')


def break_sentinize():
    data = read_data('data/break-sentinize.txt')
    sentinized_data = razdel.sentenize(data)

    list_res = list(sentinized_data)

    print(f'Amount of sentences: {len(list_res)}')
    for value in list_res:
        print(value.text)


def tokenize():
    data = read_data('data/tokenization.txt')

    print('razdel tokens')
    res_razdel = razdel.tokenize(data)
    dump_res_razdel = []
    for value in res_razdel:
        dump_res_razdel.append(value.text)
    print(dump_res_razdel)

    print('\n\nmystem tokens')
    mystem = Mystem()
    res_mystem = mystem.lemmatize(data)
    dump_res_mystem = []
    for value in res_mystem:
        if value != ' ':
            dump_res_mystem.append(value)

    print(dump_res_mystem)

    dump_data('tokens_razdel.txt', dump_res_razdel)
    dump_data('tokens_mystem.txt', dump_res_mystem)


if __name__ == '__main__':
    # break_sentinize()
    tokenize()
