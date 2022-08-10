n_1 = input('Введіть число від 3 до 9: ')
n = int (n_1)
p = input("Як вивести піраміду? (зліва, по центру)? :")
if p == "зліва":
    if n_1.isdigit and 3 <= n <= 9:

        #  print(f'так число {n_1.isdigit}') проміжна перевірка на цифри

        for i in range(1, n + 2):
            for j in range(1, i - 1):
                print(j, end=" ")
            for j in range(i - 1, 0, -1):
                print(j, end=" ")

            print()
    else:
       print("Не вірний формат числа! Програма нажаль закінччує роботу!!!")

if p == "по центру":
    n = 7
    m = (2 * n) - 2
    for i in range(0, n):
        for j in range(0, m):
            print(end=" ")
        m = m - 1  # уменьшение m после каждого прохода цикла
        for j in range(0, i + 1):
            # вывод пирамиды из звёздочек
            print("*", end=' ')
        print(" ")
else:
    print("Не вірний формат числа! Програма нажаль закінччує роботу!!!")