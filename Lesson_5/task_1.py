while True:
    a = input('Введіть число: ')
    for i in range(len(a)):
        if a[i] == a[i + 1]:
            print('да')
            break
        else:
            print('ні')
            break
    continue

# 9 годин