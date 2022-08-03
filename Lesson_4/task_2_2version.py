import math

class_1 = int(input('Скільки учнів в першому класі? : '))

class_2 = int(input('Скільки учнів в третьому класі? : '))

class_3 = int(input('Скільки учнів в третьому класі? : '))

desk_1 = math.ceil(class_1 / 2)

desk_2 = math.ceil(class_2 / 2)

desk_3 = math.ceil(class_3 / 2)

desk_all = (desk_1 + desk_2 + desk_3)

print('Всього потрібно закупити ' + str(desk_all) + ' парт!')
