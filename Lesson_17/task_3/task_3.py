def update_hero(hero, power, Y):

    with open('hero.ini', 'r') as f1, open('hero_2.ini', 'w') as f2:
        lines = f1.readlines()

        for line in lines:
            line = line.strip()
            if "hero" in line:
                f2.write(f'hero = {hero}', end="\r\n")
            if 'power' in line:
                f2.write(f'power = {power}', sep=' ')
            if 'Y' in line:
                f2.write(f'Y = {Y}')
            else:
                f2.write(line)

    with open('hero.ini', 'w') as f1, open('hero_2.ini', 'r') as f2:
        f1.write(f2.read())


if __name__ == "__main__":
    hero = input('Введіть  hero: ')
    power = input('Введіть power: ')
    Y = input('Введіть Y: ')
    update_hero(hero, power, Y)
