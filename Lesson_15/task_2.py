def dict_handler(dict, key, default_value):
    """
    Dict_handler - це навчальна функція, яка демонструє роботу з винятками в Python.

    :param dict: словник
    :param key: ключ (не змінний тип даних)
    :param default_value: значення за замовчуванням
    :return: dict (словник)
    """
    try:
        try:
            print(f'Ключ {key} в словнику є. Значення: {dict[key]}')

        except TypeError:
            raise TypeError('Помилка! Ви ввели змінюваний тип даних: ')

        except KeyError as err:
            print("Такий ключ в словнику відсутній. Додаємо: ", err)
            dict.update({key: default_value})

        finally:
            print("Dict", dict)

    except TypeError as msg:
        print(TypeError, msg, key)

    return dict


if __name__ == "__main__":
    dict = {}
    dict_handler(dict, 'f', 33)
    dict_handler(dict, 'r', 757)
    dict_handler(dict, 'r', 757)  # якщо ключ вже є в словнику (повтор попереднього)
    dict_handler(dict, {888, 99}, 88)  # змінюваний тип даних (виклик "raise")
