"""
Створюється матриця (двовимірний список) М х N.
M та N задає користувач з клавіатури.

Матриця створюється з допомогою list comprehension. При створенні, список
заповнюється випадковими числами.

Функція sum() НЕ використовується.

"""

from random import randint as rnd

m = int(input("Введіть кількість колонок M: "))
n = int(input("Введіть кількість рядків N: "))

matrix = [[rnd(10, 100) for i in range(0, m)] for j in range(0, n)]  # matrix list comprehension

print()  # space

for i in range(n):  # цикл cума рядків
    w = 0  # додаткова змінна
    for j in range(m):
        w += matrix[i][j]
    print(*matrix[i], '', w, sep='  ')

print()  # space

for i in range(m):  # цикл cума колонок
    w = 0
    for j in range(n):
        w += matrix[j][i]
    print('{:>2}'.format(w), end=' ')  # форматування виводу

print()  # space
print()  # space
