def read_file():
    info = []
    with open('file', 'r') as f:
        for line in f:
            info += line.strip("\n").split(' ')
    ans = [int(el) for el in info if el.isdigit()]
    return ans


data = read_file()


def minimum(info):
    res = info[0]
    for m in range(len(info)):
        if info[m] <= res:
            res = info[m]
    return res


def maximum(info):
    res = info[0]
    for s in range(len(info)):
        if info[s] >= res:
            res = info[s]
    return res


def addition(info):
    res = 0
    for l in range(len(info)):
        res += info[l]
    return res


def multiplication(info):
    res = 1
    try:
        for n in range(len(info)):
            res *= info[n]
    except OverflowError:
        return 'Для корректной работы функции скорректируйт входные данные'
    else:
        return res


ans_1, ans_2, ans_3 = '', '', ''
for i in data:
    ans_1 += str(i) + ' '
    ans_2 += str(i) + '+'
    ans_3 += str(i) + '*'
print(
    f'В файле: {ans_1}\n'
    f'Минимальное: {minimum(data)}\n'
    f'Максимальное: {maximum(data)}\n'
    f'Сумма: {addition(data)} ({ans_2})\n'
    f'Произведение: {multiplication(data)} ({ans_3})\n'
)
