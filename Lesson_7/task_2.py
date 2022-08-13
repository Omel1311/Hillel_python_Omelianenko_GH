while True:
    q = input('Введіть список із цілих чисел: ')
    a = list(q)
    k = int(input('Введіть число (індекс К): '))
    c = int(input('Введіть значення (число С): '))

    if k <= len(q):
        print("*" * 60)
        print(f"Було: {a}")
        a.append(3) # можна ввести будь-яке значеня.
        print(f"Проміжне значення: {a}")

        for i in range(len(a) - 1, k, -1):
            a[i] = a[i - 1]
        a[k] = c
        print(f"Cтало:{a}")
        print("*"*60)

    else:
        print("Завеликий індекс (K)! Введіть ще раз")