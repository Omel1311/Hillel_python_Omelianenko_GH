"""
    Гра морський бій (10Х10). Класичні правила (гравець/комп'ютер).

    В грі використовується 6 класів (PartBoard,Cell, Board, Game, Player, Ship)

    Шляхом надання клітинкам поля коефіціента значимості (ваги) в грі реалізовано елементи штучного інтелекту
    (компютер розрізняє клітинки, де з великою вірогідністю можуть знаходитись кораблі гравця).
    Вага клітинок оновлюється після кожного пострілу.

    В грі є 3 статуси, які визначають подальший напрямок функціонування:
    1)'prepare'
    2)'in game'
    3) "game over"

    Значення на полі:
    пуста клітинка (море) = '🟦'
    корабель гравця       = '🟧'
    потоплений корабель    = '🟥'
    підбитий корабель     = '🟥'
    невлучний постріл або сіра зона (частина поля, що не може бути використана) = '🟩'
"""

import os  # використовується для виклику функції очистки екрану
from random import *  # використовується для формування рандомних координат


class PartBoard:
    """
    Основний клас, який розділяє клас "Поле" на 3 частини:
         гравець,
         компютер,
         вага клітинок (використовується для аналізу ходу)


    """
    user = 'частина гри гравця'
    computer = ' частина гри компютера'
    weight = 'значимість клітинки поля'


class Board:
    """
    Клас, який використовуэться для створення дошок та клітинок"
    """
    def __init__(self, size):
        """
        Конструктор, в якому щоразу формуються основні параметри частин поля

        """
        self.size = size
        self.map_user = [[Cell.empty_cell for _ in range(size)] for _ in range(size)]
        self.map_comp = [[Cell.empty_cell for _ in range(size)] for _ in range(size)]
        self.weight = [[1 for _ in range(size)] for _ in range(size)]

    def get_board_part(self, element):
        """
        Метод з обовязковим праметром 'element', який дає змогу повернути значення
        інших обєктів до однієї з 3 частин поля ('частина гри гравця', частина гри компютера',
        'значимість (вага) клітинки поля')


        """
        if element == PartBoard.user:
            return self.map_user
        if element == PartBoard.computer:
            return self.map_comp
        if element == PartBoard.weight:
            return self.weight

    def create_board(self, element):
        """
        Метод, який свторює та виводить в термінал поля гравця та комп'ютера (окремо щодо поля та ваги клітинок)

        """

        field = self.get_board_part(element)
        weights = self.get_max_weight_cells()  # max_weight = 0

        if element == PartBoard.weight:
            for x in range(self.size):
                for y in range(self.size):
                    if (x, y) in weights:
                        print('\033[1;32m', end='')
                    if field[x][y] < self.size:
                        print(" ", end='')
                    if field[x][y] == 0:
                        print(str("" + "."" " + ""), end=' ')
                    else:
                        print(str("" + str(field[x][y]) + " "), end='')
                    print('\033[0;0m', end='')
                print()

        else:
            for x in range(-1, self.size):
                for y in range(-1, self.size):
                    if x == -1 and y == -1:
                        print("  ", end="")
                        continue
                    if x == -1 and y >= 0:
                        print(y + 1, end=" ")
                        continue
                    if x >= 0 and y == -1:
                        print(Game.abc[x], end=' ')
                        continue
                    print("" + str(field[x][y]), end='')
                print("")
        print("")

    def check_position_ship(self, ship, element):
        """
        Метод здійснює перевірку можливості розміщення корабля в конкретному місці
        (використвоується при розміщенні кораблів та вирахування значимості (ваги) клітинок).
        Повератє булеве значення.

        """

        field = self.get_board_part(element)

        if ship.x + ship.height - 1 >= self.size or ship.x < 0 or \
                ship.y + ship.width - 1 >= self.size or ship.y < 0:
            return False

        x = ship.x
        y = ship.y
        width = ship.width  # ширина корбаля (по Х)
        height = ship.height  # вистота корабля (по Y)

        for p_x in range(x, x + height):
            # цикл для перевірки чи не відповідають координати сірій зоні або вже відстріляним координатам.
            # Якщо так - повертає  False
            for p_y in range(y, y + width):
                if str(field[p_x][p_y]) == Cell.miss_cell:
                    return False

        for p_x in range(x - 1, x + height + 1):
            # цикл для перевірки чи не відповідають координати сірій зоні або вже відстріляним координатам.
            # Якщо так - повертає  False
            for p_y in range(y - 1, y + width + 1):
                if p_x < 0 or p_x >= len(field) or p_y < 0 or p_y >= len(field):
                    continue  # якщо координати знаходяться в межах поля - продовжує
                if str(field[p_x][p_y]) in (Cell.ship_cell, Cell.destroyed_ship):
                    return False

        return True

    def mark_destroyed_ship(self, ship, element):
        """
        Метод надає клітинкам статус "підбитго корабля" та сірої зони
        """

        field = self.get_board_part(element)

        x, y = ship.x, ship.y
        width, height = ship.width, ship.height

        for p_x in range(x - 1, x + height + 1):
            for p_y in range(y - 1, y + width + 1):
                if p_x < 0 or p_x >= len(field) or p_y < 0 or p_y >= len(field):
                    continue
                field[p_x][p_y] = Cell.miss_cell

        for p_x in range(x, x + height):
            for p_y in range(y, y + width):
                field[p_x][p_y] = Cell.destroyed_ship

    def add_ship_to_board(self, ship, element):
        """
        Метод додавання корабля на поле (формуєм коордианати шляхом пеербирання його висоти та ширини через цикл)
        """

        field = self.get_board_part(element)

        x, y = ship.x, ship.y
        width, height = ship.width, ship.height

        for p_x in range(x, x + height):
            for p_y in range(y, y + width):
                field[p_x][p_y] = ship  # по коорднатам поля додаємо корабель

    def get_max_weight_cells(self):
        """
        Метод повертає список координат із самим більшим шансом попадання.
         Перебираємо через цикли всі клітини та заносимо їх до словника weights = {} з ключем,
         який є значенням в клітинці. Через append додаємо (запамятовуємо) максимальне значення.

        """
        weights = {}  # формуємо список
        max_weight = 0

        for x in range(self.size):
            for y in range(self.size):
                if self.weight[x][y] > max_weight:
                    max_weight = self.weight[x][y]
                weights.setdefault(self.weight[x][y], []).append((x, y))

        return weights[max_weight]

    def recalculate_weight_map(self, available_ships):
        """
        Метод перераховує значення (вагу) клітинок, оскільки після кожного ходу їх вага змінюється.
        Всім клітинкам зпочатку надається значення 1.
        Пробігаємо по всьому полю.
        Якщо знаходимо поранений корабель - ставимо клітинам вище/нижче/з боків коефіцієнти помножені на 50
        (є великий шанс, що там є продовження корабля).
        За діагоналями від пораненої клітини нічого не може бути – туди вписуємо нулі.
        Якщо на карті знищений корабель або клітка з промахом - ставимо туди коефіцієнт 0.
        Далі переходимо до наступної клітини. Якщо в клітині є можливість поміститися кораблю додаємо їй коеф 1.
        """
        self.weight = [[1 for _ in range(self.size)] for _ in range(self.size)]

        for x in range(self.size):
            for y in range(self.size):
                if self.map_comp[x][y] == Cell.damaged_ship:

                    self.weight[x][y] = 0

                    if x - 1 >= 0:
                        if y - 1 >= 0:
                            self.weight[x - 1][y - 1] = 0
                        self.weight[x - 1][y] *= 50
                        if y + 1 < self.size:
                            self.weight[x - 1][y + 1] = 0

                    if y - 1 >= 0:
                        self.weight[x][y - 1] *= 50
                    if y + 1 < self.size:
                        self.weight[x][y + 1] *= 50

                    if x + 1 < self.size:
                        if y - 1 >= 0:
                            self.weight[x + 1][y - 1] = 0
                        self.weight[x + 1][y] *= 50
                        if y + 1 < self.size:
                            self.weight[x + 1][y + 1] = 0

        for ship_size in available_ships:

            ship = Ship(ship_size, 1, 1, 0)
            # перебираємо клітики поля
            for x in range(self.size):
                for y in range(self.size):
                    if self.map_comp[x][y] in (Cell.destroyed_ship, Cell.damaged_ship, Cell.miss_cell) \
                            or self.weight[x][y] == 0:
                        self.weight[x][y] = 0
                        continue
                    # перевіряємо в якій позиції може розміститись корабель
                    for rotation in range(0, 4):
                        ship.set_position(x, y, rotation)
                        if self.check_position_ship(ship, PartBoard.computer):
                            self.weight[x][y] += 1


class Cell:
    """
    Клас в якому визначений формат клітинок в залежності від їх статусу (5)
    """
    empty_cell = '🟦'
    ship_cell = '🟧'
    destroyed_ship = '🟥'
    damaged_ship = '🟥'
    miss_cell = '🟩'

class Game:
    abc = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")
    ships_rules = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
    field_size = len(abc)

    def __init__(self):

        self.players = []
        self.current_player = None
        self.next_player = None

        self.status = 'prepare'

    # при старте игры назначаем текущего и следующего игрока
    def start_game(self):
        """
        Метод старту гри. З початку визначається поточний гравець
        """
        self.current_player = self.players[0]
        self.next_player = self.players[1]

    # функция переключения статусов
    def status_check(self):
        """
        Метод переключає статус гри. Переключаємо з "prepare" на "in game" якщо до гри доданго 2 гравця.
        Далі стартуємо гру

        """
        if self.status == 'prepare' and len(self.players) >= 2:
            self.status = 'in game'
            self.start_game()
            return True
        # переключаємо в статус game over якщо у наступного гравця заишилось 0 кораблів
        if self.status == 'in game' and len(self.next_player.ships) == 0:
            self.status = 'game over'
            return True

    def add_player(self, player):
        """
        Метод, який добавялє гравця та створює поле
        """
        player.field = Board(Game.field_size)
        player.enemy_ships = list(Game.ships_rules)
        # розставляємо кораблі
        self.ships_setup(player)
        #   вираховуємо вагу для клітин поля
        player.field.recalculate_weight_map(player.enemy_ships)
        self.players.append(player)

    def ships_setup(self, player):
        """

        Метод робить розстановку кораблів за правилами, визначенимі в класі Game
        """

        for ship_size in Game.ships_rules:
            # задаємо кількість спроб виставлення кораблів (40) Щоб не потрапити в бескінечний цикл
            retry_count = 40

            ship = Ship(ship_size, 0, 0, 0)

            while True:

                Game.clear_screen()
                if player.auto_ship_setup is not True:
                    player.field.create_board(PartBoard.user)
                    player.message.append('Куди поставити {} корабель: '.format(ship_size))
                    for _ in player.message:
                        print(_)
                else:
                    print('...')

                player.message.clear()

                x, y, r = player.get_input('ship_setup')
                # якщо гравець ввів некоректні координати (зачення = 0), то просимо повторно ввести
                if x + y + r == 0:
                    continue

                ship.set_position(x, y, r)

                # якщо корабель міститься на заданій позиції - додаємо гравцю на поле корабель
                # також додаємо корабель до списку кораблів гравця і переходимо до наступного корабля для розміщення
                if player.field.check_position_ship(ship, PartBoard.user):
                    player.field.add_ship_to_board(ship, PartBoard.user)
                    player.ships.append(ship)
                    break

                player.message.append('Невірна розстановка!')
                retry_count -= 1
                if retry_count < 0:
                    # після заданої кількості невдалих спроб - обнулюємо карту гравця
                    # прибираємо всі кораблі і починаємо розстановку по новій
                    player.field.map_user = [[Cell.empty_cell for _ in range(Game.field_size)] for _ in
                                             range(Game.field_size)]
                    player.ships = []
                    self.ships_setup(player)
                    return True

    def draw(self):
        if not self.current_player.is_ai:
            self.current_player.field.create_board(PartBoard.user)
            self.current_player.field.create_board(PartBoard.computer)
            # тут можна дізнатись вагу клітинок:
            # self.current_player.field.create_board(Part_Board.weight)
        for line in self.current_player.message:
            print(line)

    def switch_players(self):
        """
        Метод заміни гравців
        """
        self.current_player, self.next_player = self.next_player, self.current_player

    @staticmethod
    def clear_screen():
        """
       Метод очистки екрану (працює з включеним "Emulate terminal")
        """

        os.system('cls' if os.name == 'nt' else 'clear')


class Player:

    def __init__(self, name, is_ai, skill, auto_ship):
        self.name = name
        self.is_ai = is_ai
        self.auto_ship_setup = auto_ship
        self.skill = skill
        self.message = []
        self.ships = []
        self.enemy_ships = []
        self.field = None

    def get_input(self, input_type):
        """
        Метод прийняття ходу гравця. Або розстанока кораблів (input_type == "ship_setup")
        або постріл (input_type == "shot")
        """

        if input_type == "ship_setup":

            if self.is_ai or self.auto_ship_setup:
                user_input = str(choice(Game.abc)) + str(randrange(0, self.field.size)) + choice(["H", "V"])
            else:
                user_input = input().upper().replace(" ", "")

            if len(user_input) < 3:
                return 0, 0, 0

            x, y, r = user_input[0], user_input[1:-1], user_input[-1]

            if x not in Game.abc or not y.isdigit() or int(y) not in range(1, Game.field_size + 1) or \
                    r not in ("H", "V"):
                self.message.append('Помилка при введенні координат!')
                return 0, 0, 0

            return Game.abc.index(x), int(y) - 1, 0 if r == 'H' else 1

        if input_type == "shot":

            if self.is_ai:
                if self.skill == 1:
                    x, y = choice(self.field.get_max_weight_cells())
                if self.skill == 0:
                    x, y = randrange(0, self.field.size), randrange(0, self.field.size)
            else:
                user_input = input().upper().replace(" ", "")
                x, y = user_input[0].upper(), user_input[1:]
                if x not in Game.abc or not y.isdigit() or int(y) not in range(1, Game.field_size + 1):
                    self.message.append('Помилка при введенні координат!')
                    return 500, 0
                x = Game.abc.index(x)
                y = int(y) - 1
            return x, y

    def make_shot(self, target_player):

        sx, sy = self.get_input('shot')

        if sx + sy == 500 or self.field.map_comp[sx][sy] != Cell.empty_cell:
            return 'retry'

        shot_res = target_player.receive_shot((sx, sy))

        if shot_res == 'miss':
            self.field.map_comp[sx][sy] = Cell.miss_cell

        if shot_res == 'get':
            self.field.map_comp[sx][sy] = Cell.damaged_ship

        if type(shot_res) == Ship:
            destroyed_ship = shot_res
            self.field.mark_destroyed_ship(destroyed_ship, PartBoard.computer)
            self.enemy_ships.remove(destroyed_ship.size)
            shot_res = 'kill'

        # після вистрілу перераховуємо ваги клітинок
        self.field.recalculate_weight_map(self.enemy_ships)

        return shot_res

    def receive_shot(self, shot):

        sx, sy = shot

        if type(self.field.map_user[sx][sy]) == Ship:
            ship = self.field.map_user[sx][sy]
            ship.hp -= 1

            if ship.hp <= 0:
                self.field.mark_destroyed_ship(ship, PartBoard.user)
                self.ships.remove(ship)
                return ship

            self.field.map_user[sx][sy] = Cell.damaged_ship
            return 'get'

        else:
            self.field.map_user[sx][sy] = Cell.miss_cell
            return 'miss'


class Ship:

    def __init__(self, size, x, y, rotation):

        self.size = size
        self.hp = size
        self.x = x
        self.y = y
        self.rotation = rotation
        self.set_rotation(rotation)

    def __str__(self):
        return Cell.ship_cell

    def set_position(self, x, y, r):
        self.x = x
        self.y = y
        self.set_rotation(r)

    def set_rotation(self, r):
        self.rotation = r

        if self.rotation == 0:
           self.width = self.size
           self.height = 1
        elif self.rotation == 1:
            self.width = 1
            self.height = self.size
        elif self.rotation == 2:
            self.y = self.y - self.size + 1
            self.width = self.size
            self.height = 1
        elif self.rotation == 3:
            self.x = self.x - self.size + 1
            self.width = 1
            self.height = self.size


if __name__ == '__main__':
    players = []
    players.append(Player(name='Гравець', is_ai=False, auto_ship=True, skill=1))
    players.append(Player(name="Комп'ютер", is_ai=True, auto_ship=True, skill=1))

    game = Game()  # запуск гри + додаємо безкінечний цик While

    while True:
        game.status_check()  # кожен початок ходу перевіряємо статус і далі вже діємо виходячи зі статусу гри

        if game.status == 'prepare':
            game.add_player(players.pop(0))  # додаємо гравця

        if game.status == 'in game':

            Game.clear_screen()  # очищаємо екран та додаємо повідомлення для поточного гравця та малюємо гру
            game.current_player.message.append("Введіть координати для пострілу (приклад: 'a2'): ")
            game.draw()
            # очищаємо список повідомлень для гравця
            game.current_player.message.clear()  # чекаємо результ
            # результат пострілу
            shot_result = game.current_player.make_shot(game.next_player)

            if shot_result == 'miss':\

                game.next_player.message.append('{} промахнувся! '.format(game.current_player.name))
                game.next_player.message.append('Хід: -> {}!'.format(game.next_player.name))
                game.switch_players()
                continue
            elif shot_result == 'retry':
                game.current_player.message.append('Спробуйте ще раз!')
                continue
            elif shot_result == 'get':
                game.current_player.message.append('Влучили!')
                continue
            elif shot_result == 'kill':
                game.current_player.message.append('Корабeль знищено!')
                game.next_player.message.append('Корабель був повністю знищений!')
                continue

        if game.status == 'game over':
            Game.clear_screen()
            game.next_player.field.create_board(PartBoard.user)
            game.current_player.field.create_board(PartBoard.user)
            print('{} переміг!'.format(game.current_player.name))
            break

    input('')
