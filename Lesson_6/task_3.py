n_1 = input('Введіть число від 3 до 9: ')

if n_1.isdigit():
    n = int(n_1)
    if 3 <= n <= 9:
        p = input("Як вивести піраміду? ('зліва', 'по центру')? :")  # зправа - ще доопрацьовую


        if p == "зліва":
            #  print(f'так число {n_1.isdigit}') проміжна перевірка на цифри

            for i in range(1, n + 2):
                for j in range(1, i - 1):
                    print(j, end=" ")
                for j in range(i - 1, 0, -1):
                    print(j, end=" ")
                print()

        elif p == "по центру":
            m = (2 * n) - 2
            for i in range(0, n):
                for j in range(0, m):
                    print(end=" ")
                m = m - 1
                for j in range(1, i + 2):
                    print(j, end=' ')
                print()
        else:
            print("Не вірний формат числа! Програма, нажаль, закінччує роботу!!!1")
    else:
        print("Не вірний формат числа! Програма, нажаль, закінччує роботу!!!2")

else:
    print("Не вірний формат числа! Програма, нажаль, закінчує роботу!!!3")