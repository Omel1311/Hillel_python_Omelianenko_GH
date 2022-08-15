import random

#n = int(input('Введіть число: '))
n = 5
Matrix = [[random.randint(0, 10) for x in range(n)] for y in range(n)]

for x in range(n):
    print(Matrix[x])


s = [sum(i) for i in zip(*Matrix)]
print(s[n-1])
print(s)


s_2 = [sum(1) for i in zip(*Matrix)]
print(s_6[n-1])
print(s)