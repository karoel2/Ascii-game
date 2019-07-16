from objects import *
from getch import *
from termcolor import colored #ON WINDOWS FIRST os.system('color')
import random
import time
from objects2 import *



class Cords():
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, x, y):
        self.x += x
        self.y += y


class Game():

    def __init__(self, player, map):
        self.player = player
        self.map = map
        global console
        console = Player_Console(player)


    def move(self):
        char = getch().lower()
        if char == 'a':
            self._do_move(-1, 0)
        elif char == 'w':
            self._do_move(0, -1)
        elif char == 'd':
            self._do_move(1, 0)
        elif char == 's':
            self._do_move(0, 1)


    def _do_move(self, x, y):
        block = self._chceck_collision(self.player.player_cords, x, y)
        if block.exp()[0] == 3:
            block.shop()
        elif block.exp()[0] == 2:
            self.player.hull.dmg(block.exp()[1])
            if self.player.hull.death():
                self._dig(block, x, y)
                self.player.player_cords.update(y, x)
                self._after_dig()
        elif block.exp()[0] == 1:
            if(block.worth != 0):
                self.player.cargo_bay.add(block)
            self._dig(block, x, y)
            self.player.player_cords.update(y, x)
            self._after_dig()
        elif block.exp()[0] == 0:
            self.move


    def _chceck_collision(self, cords, x, y):
        block = None
        if y is not 0:
            if y > 0:
                block = self.map.list[cords.x + 1][cords.y]
            else:
                block = self.map.list[cords.x - 1][cords.y]
        if x is not 0:
            if x > 0:
                block = self.map.list[cords.x][cords.y + 1]
            else:
                block = self.map.list[cords.x][cords.y - 1]
        return block

    def _dig(self, block, x = 0, y = 0):
        self.map.create_player_map(self.player.player_cords)
        self.map.insert_drill(x, y)
        self.map.print_player_map()
        self.player.collision(block, x, y)

    def _after_dig(self):
        self.map.create_player_map(self.player.player_cords)
        self.map.print_player_map()


class Map():
    player_map = []
    shop = None
    def set_shop(self, shop):
        self.shop = shop
        for i in range(100):
            self.list[6][i] = self.shop

    def __init__(self):
        self.list = [[self._generate() for _ in range(100)] for _ in range(100)]

        for i in range(100):
            self.list[i][6] = Wall()
            self.list[i][94] = Wall()
            for j in range(6):
                self.list[j][i] = Mineral('grey', 'air', 0)
        for i in range(100):
            for j in range(6):
                self.list[i][j] = Mineral('grey', 'air', 0)

    def _generate(self):
        i = random.randint(0, 1000)
        if i < 10:
            return Artefact()
        elif i < 20:
            return Mineral('cyan', 'diamond', 5, 2000)
        elif i < 40:
            return Mineral('magenta', 'cristal', 4, 1500)
        elif i < 70:
            return Mineral('blue', 'lapis', 3, 750)
        elif i < 100:
            return Mineral('green', 'jade', 2, 300)
        elif i < 200:
            return Mineral('yellow', 'gold', 1.5, 100)
        elif i < 235:
            return Lava()
        elif i < 270:
            return Bedrock()
        else:
            return Mineral()


    def create_player_map(self, cords):
        slice = [self.list[i][cords.y - 5 : cords.y + 6] for i in range(cords.x - 5 , cords.x + 6)]
        slice[5][5] = "☼"
        self.player_map = slice

    def insert_drill(self, x = 0, y = 0):
        if y is not 0:
            if y > 0:
                self.player_map[6][5] = '▾'
            else:
                self.player_map[4][5] = '▴'
        if x is not 0:
            if x > 0:
                self.player_map[5][6] = '▸'
            else:
                self.player_map[5][4] = '◂'

    def print_player_map(self):
        console(player_map = self.player_map, print = True)

class Player():
    """docstring for Player."""

    def earn(self, money):
        self.money += money


    def __init__(self, map):
        self.player_cords = Cords(7, 50)
        self.money = 0
        self.air = Mineral('grey', 'air', 0)
        self.map = map
        self.fuel_tank = Fuel_Tank(10, 'Basic',  32)
        self.cargo_bay = Cargo_Bay(10, 'Basic', 15)
        self.engine = Engine(10, 'Basic', 1.0)
        self.drill = Drill(10, 'Basic', 1.0)
        self.hull = Hull(10, 'Basic', 8)


    def collision(self, obj, x, y):

        if obj.hardeness is 0:
            time.sleep(0.1/self.engine.speed)
            self.fuel_tank.loss(0.1)

        else:
            time.sleep(obj.hardeness/self.drill.effecitvity)
            self.fuel_tank.loss(obj.hardeness)
        self.map.list[self.player_cords.x][self.player_cords.y] = self.air



class Player_Console():

    def print_console(self):
        print(*self.player.hull.print_hull() + ['       '] + self.player.fuel_tank.print_fuel(), sep='')
        print(self.player.money, ' $')
        print('[', *self.player.cargo_bay.item_list, ']', sep='')
        for i in range(len(self.player_map)):
            print(*self.player_map[i])
        if self.text is not None:
            print(self.text)
            self.text = self.next_text
            self.next_text =  None

    def __init__(self, player):
        self.text = None
        self.next_text = None
        self.player = player
        print("start")

    def __call__(self, **kwargs):

        if 'player_map' in kwargs:
                self.player_map = kwargs['player_map']
        if 'text' in kwargs:
                self.text = kwargs['text']
        if 'next_text' in kwargs:
                self.next_text = kwargs['next_text']
        if 'print' in kwargs:
            clear()
            self.print_console()
