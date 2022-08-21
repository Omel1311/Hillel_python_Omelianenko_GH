newspaper = 75
magazine = 27
newspaper_and_magazine = 13

number_family = (newspaper-newspaper_and_magazine) + (magazine-newspaper_and_magazine) + newspaper_and_magazine
print('*'*60)
print(f'(спосіб 1) В будинку проживає {number_family} сімей')

#  спосіб 2 (з використанням множин)

newspaper_1 = {newspaper - newspaper_and_magazine}
magazine_1 = {magazine - newspaper_and_magazine}
newspaper_and_magazine_1 = {newspaper_and_magazine}

print('*'*60)
total = sum(newspaper_1 | magazine_1 | newspaper_and_magazine_1)
print(f'(спосіб 2) В будинку проживає {total} сімей')


