def test_1(n, *f):
    for i in f:
        for j in f:
            if i + j == n:
                print(f'Тест 1: сума {i, j} = {n}')
                return n, f


def test_2(v, *t):
    for q in t:
        for w in t:
            if q + w == v:
                print(f'Тест 2: сума {q, w} = {v}')
                return v, t


test_1(3, 2, 4, 1)
test_1(100, 40, 50, 5, 30, 30)
test_2(3, 3, 1, 2, 2)
test_2(6, 3, 3, 3, 3, 3, 3)
