n = max_number = min_number = total = int(input("Введіть будь-ласка число: "))
even_1numbers = 0
even_2numbers = 0
noteven_1numbers = 0
noteven_2numbers = 0
number_of_numbers = 0
d = n % 2  # вирахвуємо парність до початку циклу
#  print("d" + str(d)) контрольна перевірка парності чисел до циклу
if d == 0:
    even_1numbers = 1

if d == 1:
    noteven_1numbers = 1

#  print("1 парн" + str(even_1numbers)) контрольна перевірка НЕпарності чисел до циклу

while True:
    n = int(input('Введіть будь-луска число: '))
    total += n
    number_of_numbers += 1
    arithmetic_mean = total / number_of_numbers

    d_2 = n % 2  # вирахвуємо парність в циклі

    if d_2 == 0 and n != 0:
        even_2numbers += 1
        #  print("2 парн" + str(кільк_2парних)) контрольна перевірка парності чисел в циклі

    if d_2 == 1 and d_2 != 0:
        noteven_2numbers += 1
        #  print("2 непарн" + str(even_2numbers)) контрольна перевірка непарності чисел в циклі

    if n > max_number and n != 0:
        max_number = n

    if n < min_number and n != 0:
        min_number = n

    if n == 0:
        print("Максимальне число: " + str(max_number))
        print("Мінімальне число: " + str(min_number))
        print("Сума всіх числел: " + str(total))
        sum_all_even_numbers = even_1numbers + even_2numbers
        sum_all_noteven_numbers = noteven_1numbers + noteven_2numbers
        print("Всьогот парних числел: " + str(sum_all_even_numbers))
        print("Всьогот НЕпарних числел: " + str(sum_all_noteven_numbers))
        print("Середнє арифметичне: " + str(arithmetic_mean))
        break

# 8 годин
