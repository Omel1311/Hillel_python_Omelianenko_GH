while True:
    count_duplicate_symbol = 0
    while True:
        input_list_1 = input('Введіть числа до списку 1: ')
        input_list_2 = input('Введіть числа до списку 2: ')

        len_1 = len(input_list_1)
        len_2 = len(input_list_2)

        for i in range(len_1):
            for j in range(len_2):
                if input_list_1[i] == input_list_2[j]:
                    count_duplicate_symbol += 1
                    #  print(count_duplicate_symbol) контрольна перевірка дублюючих символів

        count_unique_symbol = (len_1+len_2)-(count_duplicate_symbol*2)

        print(f'Всього у двох списках унікальних символів: {count_unique_symbol}')

        print("*"*60)

        break

#  2 год
