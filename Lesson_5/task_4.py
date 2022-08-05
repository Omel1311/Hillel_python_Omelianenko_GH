n = int(input("Введіть будь-ласка ціле число: "))

max_range = n ** 2

i = 0

for i in range(1, max_range):
    i **= 2
    if i <= n:
        print(i)

    continue

#  20 хвилин
