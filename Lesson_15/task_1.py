def exception(a, n):
    """
    Exception - це навчальна функція, яка демонструє роботу з винятками в Python.

    Використовуючи обробку винятків, функція запитує введення двох значень. Якщо хоча
    б одне з них не є числом, виконується конкатенація. В інших випадках введені
    числа підсумовуються.

    :param a:  для перевірки необхідно ввести не число (зпрацює except)
    :param n:  для перевірки необхідно ввести не число (зпрацює except)
    :return:  s

    """

    try:
        a = int(a)
        n = int(n)
        s = a + n

    except (ValueError, TypeError):  # або залишити except Exception
        print()
        s = str(a + n)
        print(f'конкатенація: {s}')
    else:
        print()
        print(f'Сума {s}')
    finally:
        print()
        print("Дякуємо за увагу!")

    return s


if __name__ == "__main__":
    b = input('Введіть число А: ')
    c = input('Введіть число N: ')
    exception(b, c)
