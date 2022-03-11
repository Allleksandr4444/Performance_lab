try:
    n, m = map(int, input('Введите 2 целых числа через пробел: ').split())
except:
    print('Необходимо ввести 2 целых числа через пробел.')

def list_result(n, m):
    list_all = []
    circular_array = str(m * ''.join([str(i) for i in range(1, n + 1)]))
    list_one = ' '
    start = 0
    stop = m
    result = ''
    while list_one[-1] != '1':
        list_one = circular_array[start:stop]
        list_all.append(list_one)
        start += m - 1
        stop += m - 1
    for i in list_all:
        result += i[0]
    return result


if __name__ == "__main__":
    print(list_result(n, m))
