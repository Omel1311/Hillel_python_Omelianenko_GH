class_1 = int(input('Скільки учнів в першому класі? : '))

class_2 = int(input('Скільки учнів в третьому класі? : '))

class_3 = int(input('Скільки учнів в третьому класі? : '))

desk_1 = class_1 // 2

desk_11 = class_1 % 2

desk_111 = desk_1 + desk_11

desk_2 = class_2 // 2

desk_22 = class_2 % 2

desk_222 = desk_2 + desk_22

desk_3 = class_3 // 2

desk_33 = class_3 % 2

desk_333 = desk_3 + desk_33

desk_all = (desk_111 + desk_222 + desk_333)

print('Всього потрібно закупити ' + str(desk_all) + ' парт!')
