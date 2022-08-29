def test_1(n, *f):
    rez = False
    for i in f:
        for j in f:
            if i + j == n:
                rez = True
    print(f'Тест 1: {rez}')
    return rez


test_1(3, 2, 4, 1)
test_1(9, 88, 9, 5, 4, 8)
test_1(9, 2, 1)
