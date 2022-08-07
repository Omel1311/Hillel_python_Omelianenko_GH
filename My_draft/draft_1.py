while True:
    a = input('Введіть число: ')
    y = list(a)
    for i in range(len(y)):
        for j in range(len(y)):
            if y[i] == y[j]:
                if i != j:
                    print('ТАК')
                    break




