while True:
    q = input('Введіть список із цілих чисел: ')
    a = list(q)
    k = int(input('Введіть число (індекс К): '))

    if k <= len(q):
        c = int(input('Введіть значення (число С): '))
        ap = input("Введіть значення, яке буде додано в кінці списку: ")
        print("*" * 60)
        print(f"Було: {a}")

        for i in range(len(a) - 1, k, -1):
            a[i] = a[i - 1]

        a[k] = c
        a.append(ap)
        print(f"Cтало:{a}")
        print("*"*60)
    else:
        print("Завелике число! Введіть ще раз")