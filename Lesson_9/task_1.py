dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}

dictionary_1.update(dictionary_2)  # cgj

print(f'спосіб 1: {dictionary_1}')

dictionary_3 = {**dictionary_1, **dictionary_2}

print(f'спосіб 2 (зі створенням нового словника dictionary_3) : {dictionary_3}')