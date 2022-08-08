while True:

    words_input = input('Введіть два слова через пробіл: ')
    number_words = len(words_input.split())

    while number_words == 2:
        reverse = words_input[::-1]
        tile = reverse.title()
        print(tile)

        break
