import random

#n = int(input('Введіть число: '))
n = 5
Matrix = [[random.randint(0,100) for x in range(n)] for y in range(n)]

for x in range(n):
    print(Matrix[x])

    s = sum(Matrix[3])

