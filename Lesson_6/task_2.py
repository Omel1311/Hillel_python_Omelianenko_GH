while True:
    string = input('Введіть рядок: ')
    char = input('Введіть символ: ')

    while char in string:
        print('Індекс(и) символу: ')
        for i in range(len(string)):
            if string[i] == char:
                print(string.find(char, i))
        break

    else:
        print('Такого символу в рядку не має!')
