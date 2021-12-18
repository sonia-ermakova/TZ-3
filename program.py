def read_file():
    info = []
    with open('file', 'r') as f:
        for line in f:
            info += line.strip("\n").split(' ')
    data = [int(i) for i in info if i.isdigit()]
    return data


data = read_file()


def minimum(info):
    res = info[0]
    for i in range(len(info)):
        if info[i] <= res:
            res = info[i]
    return res


def maximum(info):
    res = info[0]
    for i in range(len(info)):
        if info[i] >= res:
            res = info[i]
    return res


def addition(info):
    res = 0
    for i in range(len(info)):
        res += info[i]
    return res


def multiplication(info):
    res = 1
    try:
        for i in range(len(info)):
            res *= info[i]
    except:
        print('OverflowError')
    else:
        return res

