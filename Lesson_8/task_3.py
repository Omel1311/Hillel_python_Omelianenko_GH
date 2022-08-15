import random

random_list = [random.randint(0, 1000) for x in range(15)]
print(list(random_list))

s_1 = 0
s_2 = 0

for i in list(random_list):
    if i % 2 == 0:
        s_1 += i
    else:
        s_2 += i

if s_1 > s_2:
    print('Так: ')
    print(f"сума парних {s_1}")
    print(f"сума непарних {s_2}")
else:
    print("Ні: ")
    print(f"сума парних {s_1}")
    print(f"сума непарних {s_2}")


