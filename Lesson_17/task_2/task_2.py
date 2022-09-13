def longest_words(file):
    """
    longest_words - функція, яка виводить слово, що має максимальну довжину
    (або список слів, якщо таких кілька)

    :param file: файл
    :return: final_dict (змінна файлу)
    """

    text = open(file, 'r', encoding='utf-8')

    text_split = text.read().split()  # читаємо та форматуємо текст

    dict = {i: len(i) for i in text_split}  # створюємо словник

    #  print(dict) тестова перевірка довжини всіх слів

    max_val = max(dict.values())

    final_dict = {k: v for k, v in dict.items() if v == max_val}  # визначаємо в словнику пару з макс.значенням

    print(f'Слова з максимальною довжиною: {final_dict}')

    text.close()
    return final_dict



if __name__ == "__main__":
    file = 'article.txt'
    longest_words(file)
