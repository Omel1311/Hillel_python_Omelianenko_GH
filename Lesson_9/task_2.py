import random

random_list_1 = [x for x in range(1,21)]
#  print(list(random_list_1)) перевірка 1

random_list_2 = [random.randint(1, 100) for x in range(20)]
#  print(list(random_list_2)) перевірка 2

dict_1 = {k: v for k, v in zip(random_list_1, random_list_2)}
print(type(dict_1))
print(dict_1)

m = 1
for i in dict_1.values():
    m = i*m

print(f"Результат перемноження значень в словнику: {m}")