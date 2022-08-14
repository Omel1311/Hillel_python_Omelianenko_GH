n = int(input('Введіть число: '))

Matrix = [[x for x in range(-n, 0)] if y % 2 != 0 else ([y]*n) for y in range(n)]

for y in range(n):
    print(Matrix[y])
