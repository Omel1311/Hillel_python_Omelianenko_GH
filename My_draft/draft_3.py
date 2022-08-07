while True:
    while True:
        count_duplicate_numbers = 0
        input_number = input('Введіть число: ')
        list_number = list(input_number)

        for i in range(len(list_number)):
            for j in range(len(list_number)):
                if list_number[i] == list_number[j]:
                    if i != j:
                        count_duplicate_numbers += 1

        if count_duplicate_numbers >= 2:
            print('ТАК')
        else:
            print('НІ')
        break

# 9 + 11 годин
