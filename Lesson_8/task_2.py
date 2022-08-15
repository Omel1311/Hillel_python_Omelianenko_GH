import random

n = int(input('Введіть число: '))

Matrix = [[random.randint(0, 10) for x in range(n)] for y in range(n)]

s_d = 0  # сума по діагоналі
s_k = 0  # cума останнього стовбця

for x in range(n):
    print(Matrix[x])  # вивід матриці

for j in range(n):
    s_d += Matrix[j][j]
    s_k += Matrix[j][n-1]

print("*"*60)

print("cума чисел по діагоналі (зліва): " + str(s_d))
print("cума чисел станнього стовбця: " + str(s_k))

#  2 варіант коду щодо суми чисел матриці з "sum" та "zip"
s = [sum(i) for i in zip(*Matrix)]
print("cума чисел останнього стовбця (2 варіант коду): " + str(s[n-1]))

print("*"*60)

