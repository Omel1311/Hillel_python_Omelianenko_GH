password = 12345

user_password = int(input('Введіть будь-ласка пароль!: '))

if user_password != password:
    print("Невірно! Вам відмовлено в доступі!")
    user_password_2 = int(input('Введіть будь-ласка повторно пароль!: '))
    if user_password_2 == password:
        print("Пароль вірний! Ви отримали доступ!")
    else:
        print("Відмовлено в доступі повторно! Ви заблоковані!")
else:
    print("Пароль вірний! Ви отримали доступ!")