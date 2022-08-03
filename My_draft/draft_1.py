import random

a = random.randint(1, 5)

print(a)   # для кращого тестування програми

b = int(input("Спробуйте вгадати число від 1 до 5!: "))

if b > a:
    print('<Багато!')
else:
    if b < a:
        print('Мало!')
    else:
        print('Ви вгадали!')

x = 3

x **= 3

print(x)

