while True:
    q = input('Введіть список із чисел: ')
    a = q_1 = list(q)
    q_1 = list(q)
    k = int(input('Введіть число: '))
    len_a = len(a)

    for i in range(k + 1, len_a):
        a[i - 1] = a[i]

    a.pop()

    print(f"Було: {q_1}")
    print(f"Cтало:{a}")

    print("*"*60)
