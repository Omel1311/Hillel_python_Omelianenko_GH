def update_hero(hero, power, Y):
    """
    update_hero - функція, яка перезаписує файл новими значеннями,
    а незмінені значення залишаються незмінними.

    :param hero: ім’я героя
    :param power: int
    :param Y: float/int
    :return: f2 (перезаписані файли)

    """
    with open('hero.ini', 'r') as f1, open('hero_2.ini', 'w') as f2:
        lines = f1.readlines()

        for line in lines:
            line = line.strip()

            if "hero" in line:
                f2.write(f'hero={hero}\n')
            elif 'power' in line:
                f2.write(f'power={power}\n')
            elif 'Y' in line:
                f2.write(f'Y={Y}\n')
            else:
                f2.write(line + '\n')

    with open('hero.ini', 'w') as f1, open('hero_2.ini', 'r') as f2:
        f1.write(f2.read())

        return f2


if __name__ == "__main__":
    hero = input('Введіть  hero: ')
    power = input('Введіть power: ')
    Y = input('Введіть Y: ')
    update_hero(hero, power, Y)
