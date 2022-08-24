import random
r = random.randint(1, 10)

lst_1 = 1, 2, 3, 4, 5, 6, 7
lst_2 = 0, 8, 9, 10, 11, 12, 13
lst_3 = (list(i for i in range(1, r)))

lst_lambda_1 = list(map(lambda x, y=5: x**y, lst_1))
lst_lambda_2 = list(map(lambda x, y=5: x**y, lst_1.__add__(lst_2)))
lst_lambda_3 = list(map(lambda x, y=5: x**y, lst_1 + lst_2))
lst_lambda_4 = list(map(lambda x, y=r: x**r, lst_3))

print(f' 1 список {lst_lambda_1}')
print(f' 2 списки {lst_lambda_2}')
print(f' 2 списки 2 варіант {lst_lambda_3}')
print(f' 1 список 2 варіант random (степінь = {r}, випадковий список {lst_3}) {lst_lambda_4}')
