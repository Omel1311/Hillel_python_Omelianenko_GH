txt = '''
Любіть Україну, як сонце любіть,
як вітер, і трави, і води...
В годину щасливу і в радості мить,
любіть у годину негоди.

Любіть Україну у сні й наяву,
вишневу свою Україну,
красу її, вічно живу і нову,
і мову її солов'їну.

Без неї — ніщо ми, як порох і дим,
розвіяний в полі вітрами...
Любіть Україну всім серцем своїм
і всіми своїми ділами.'''

replace_1 = txt.replace(",", "")
replace_2 = replace_1.replace(".", "")
replace_3 = replace_2.replace("—", "")
replace_4 = replace_3.lower()

str_split = replace_4.split()  # тут відображається текст з малої літери та без розділових знаків


dict_1 = {s: str_split.count(s) for s in str_split}

lst = dict_1.items()
lst_1 = list(lst)
print("*"*160)
print(lst_1)  # повний список з ключами і значеннями

keys = list(dict_1.keys())
values = list(dict_1.values())
#  print(values) перевірка values
max_values = 1
max_keys = 0
max_values_2 = 1
max_keys_2 = 0

for i in range(len(values)):
    if values[i] > max_values:
        max_values = values[i]
        max_keys = keys[i]

a = {k: v for k, v in lst if v == 1}
min_items = a.items()
k = list(min_items)

print("*"*160)
print(f'Найбільша кількість слів: {max_keys, max_values}')
print("*"*160)
print(f'Найменша кількість слів: {k}')
print("*"*160)

