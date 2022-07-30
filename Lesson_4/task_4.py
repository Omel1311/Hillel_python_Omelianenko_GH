user_year = int(input('Введіть будь-ласка номер року для перевірки (в період з 1900 по 1_000_000)!: '))

user_year_check_4 = int(user_year) % 4

user_year_check_100 = int(user_year) % 100

user_year_check_400 = int(user_year) % 400

if 1900 < user_year or user_year > 1_000_000:
    if user_year_check_4 == 0 and user_year_check_100 != 0:
        print(str(user_year) + " - це високосний рік!")
    elif user_year_check_400 == 0:
        print(str(user_year) + " - це високосний рік!")
    else:
        print(str(user_year) + " - це НЕ високосний рік!")
else:
    print(str(user_year) + ' - введений номер року не відповідає вимогам!')
    if user_year_check_4 == 0 and user_year_check_100 != 0:
        print(str(user_year) + " - це високосний рік!")
    elif user_year_check_400 == 0:
        print('До речі, ' + str(user_year) + ' рік - це високосний рік!')
    else:
        print('До речі, ' + str(user_year) + ' рік - це НЕ високосний рік!')

print("Дякуємо за увагу!")
