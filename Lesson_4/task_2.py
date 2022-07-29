class_1 = int(input('Скільки учнів в першому класі? : '))

class_2 = int(input('Скільки учнів в третьому класі? : '))

class_3 = int(input('Скільки учнів в третьому класі? : '))

desk = (class_1+class_2+class_3) // 2

desk_all = desk + ((class_1+class_2+class_3) % 2)

print('Всього потрібно закупити ' + str(desk_all) + ' парт!')
