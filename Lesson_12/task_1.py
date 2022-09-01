import random


def column_sort_and_summ(matrix_: list, column: int, ascending: bool) -> int:
    current_column = [row[column] for row in matrix_]
    current_column.sort(reverse=ascending)
    for i in range(len(matrix_)):
        matrix_[i][column] = current_column[i]
    return sum(current_column)


def swap_colums(matrix_: list, col: int):
    for row_ in matrix_:
        row_[col], row_[col + 1] = row_[col + 1], row_[col]


m = int(input('M: '))

if m >= 5:
    matrix = [[random.randint(1, 50) for _ in range(m)] for _ in range(m)]

    asc = False
    sums = [column_sort_and_summ(matrix, i, asc := not asc) for i in range(len(matrix))]
    print('\nНе відсортована матриця\n')
    print(*matrix, sep='\n')
    print(sums)
    flag = True
    while flag:
        flag = False
        for i in range(len(sums) - 1):
            if sums[i] > sums[i + 1]:
                flag = True
                sums[i], sums[i + 1] = sums[i + 1], sums[i]
                swap_colums(matrix, i)
                continue

    print('\nВідсортована матриця\n')
    print(*matrix, sep='\n')
    print(sums)
