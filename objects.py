
from termcolor import colored #ON WINDOWS FIRST os.system('color'
import random
from objects2 import *
from getch import *
import object_game


class Block(object):
    """docstring for Block."""

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def exp(self):
        return True

    def __str__(self):
        return colored('█', self.color)

    def __repr__(self):
        return colored('█', self.color)


class Mineral(Block):
    """docstring for Stone."""

    def __init__(self, color = 'white', name = 'Stone',  hardeness = 1.0, worth = 0):
        self.name = name
        self.hardeness = hardeness
        self.color = color
        self.worth = worth

    def exp(self):
        if self.worth is not 0:
            temp = "you earn {}$ from: {}".format(self.worth, self.name)
            object_game.console(next_text = temp, text =  temp)
        return [1, self.worth]

class Bedrock(Block):

    color = 'white'
    name = 'Bedrock'

    def __init__(self):
        pass

    def __str__(self):
        return colored('■', self.color, attrs=['bold'])

    def exp(self):
        object_game.console(text = 'Can\'t dig that', print = True)
        return [0, 0]

class Wall(Block):

    color = 'white'
    name = 'Wall'

    def __init__(self):
        pass

    def __str__(self):
        return colored('|', self.color, attrs=['bold'])

    def exp(self):
        object_game.console(text = 'Can\'t dig that', print = True)
        return [0, 0]

class Lava(Block):

    hardeness = 1
    color = 'red'
    name = 'Lava'
    damage = 2

    def __init__(self):
        pass

    def __str__(self):
        return colored('■', self.color, attrs=['bold'])

    def exp(self):
        object_game.console(text = 'Oh no, you struck lava')
        return [2, self.damage]

class Artefact(Mineral):

    def __init__(self, color = 'white', name = 'Artefact',  hardeness = 1.0, worth = 10000):
        super().__init__(color = 'white', name = 'Artefact',  hardeness = 1.0, worth = 10000)
        self.sign = random.choice(['☥', '۵', '☠', 'π', '∞', 'Σ', '∆', '∵', '∅', '⍺'])

    def __str__(self):
        return colored(self.sign, self.color)

class Shop(Block):

    def __init__(self, player):
        self.player = player

    def __str__(self):
        return colored('_', 'white', attrs=['bold'])

    def exp(self):
        return [3, 0]

    def shop(self):
        self.menu()

    def sell(self):
        money = 0
        for item in self.player.cargo_bay.item_list:
            money += item.worth
        self.player.earn(money)
        self.player.cargo_bay.item_list = []

    def menu(self):
        print('1. Sell all')
        print('2. Refill')
        print('3. Buy upgrades')
        print('0. Return')
        char = getch()
        if char == '1':
            self.sell()
            object_game.console(print = True)
        if char == '2':
            temp = self.player.fuel_tank.size - self.player.fuel_tank.fuel_amount
            self.player.money -= 2 * temp
            self.player.fuel_tank.fuel_amount = self.player.fuel_tank.size
            self.player.money = int(self.player.money)
            object_game.console(print = True)
        if char == '3':
            self.buy_upgrades()
        if char == '0':
            object_game.console(print = True)


    def buy_upgrades(self):
        system('clear')
        print('1. Buy fuel_tank')
        print('2. Buy cargo_bay')
        print('3. Buy engine')
        print('4. Buy drill')
        print('5. Buy hull')
        print('0. Return')
        char = getch().lower()
        if char == '1':
            i = self.printy('fuel tank')
            if i is not 0:
                self.buy_fuel_tank(i)
        elif char == '2':
            i = self.printy('cargo bay')
            if i is not 0:
                self.buy_cargo_bay(i)
        elif char == '3':
            i = self.printy('engine')
            if i is not 0:
                self.buy_engine(i)
        elif char == '4':
            i = self.printy('drill')
            if i is not 0:
                self.buy_drill(i)
        elif char == '5':
            i = self.printy('hull')
            if i is not 0:
                self.buy_hull(i)
        elif char == '0':
            self.menu()
        else:
            self.buy_upgrades()

    def printy(self, thing):
        system('clear')
        print('1. Buy reinforced {} 100$'.format(thing))
        print('2. Buy improved {} 1000$'.format(thing))
        print('3. Buy advanced {} 5000$'.format(thing))
        print('4. Buy military class {} 20000$ '.format(thing))
        print('0. Return')
        char = getch()
        print(char)
        if char == '0':
            self.buy_upgrades()
            return 0
        elif char in ['1', '2', '3', '4']:
            return(char)
        else:
            self.printy(thing)
            return 0

    def buy_fuel_tank(self, quality):
        list = [
        [100, 'reinforced', 40],
        [1000, 'improved', 75],
        [5000, 'advanced', 100],
        [20000, 'military class', 200]
        ]
        item = list[int(quality) - 1]
        if self.player.money >= item[0]:
            self.player.fuel_tank = Fuel_Tank(item[0], item[1], item[2])
            self.player.money -= item[0]
            object_game.console(text = 'You have bought: {} fuel tank'.format(item[1]), print = True)

        else:
            object_game.console(text = 'Need more money', print = True)
            self.menu()


    def buy_cargo_bay(self, quality):
        list = [
        [100, 'reinforced', 20],
        [1000, 'improved', 35],
        [5000, 'advanced', 55],
        [20000, 'military class', 100]
        ]
        item = list[int(quality) - 1]
        if self.player.money >= item[0]:
            self.sell()
            self.player.cargo_bay = Cargo_Bay(item[0], item[1], item[2])
            self.player.money -= item[0]
            object_game.console(text = 'You have bought: {} cargo_bay'.format(item[1]), print = True)

        else:
            object_game.console(text = 'Need more money', print = True)
            self.menu()

    def buy_engine(self, quality):
        list = [
        [100, 'reinforced', 1.25],
        [1000, 'improved', 1.60],
        [5000, 'advanced', 2.0],
        [20000, 'military class', 2.75]
        ]
        item = list[int(quality) - 1]
        if self.player.money >= item[0]:
            self.player.engine = Engine(item[0], item[1], item[2])
            self.player.money -= item[0]
            object_game.console(text = 'You have bought: {} engine'.format(item[1]), print = True)

        else:
            object_game.console(text = 'Need more money', print = True)
            self.menu()

    def buy_drill(self, quality):
        list = [
        [100, 'reinforced', 1.25],
        [1000, 'improved', 1.60],
        [5000, 'advanced', 2.0],
        [20000, 'military class', 2.75]
        ]
        item = list[int(quality) - 1]
        if self.player.money >= item[0]:
            self.player.drill = Drill(item[0], item[1], item[2])
            self.player.money -= item[0]
            object_game.console(text = 'You have bought: {} drill'.format(item[1]), print = True)

        else:
            object_game.console(text = 'Need more money', print = True)
            self.menu()

    def buy_hull(self, quality):
        list = [
        [100, 'reinforced', 8],
        [1000, 'improved', 14],
        [5000, 'advanced', 22],
        [20000, 'military class', 40]
        ]
        item = list[int(quality) - 1]
        if self.player.money >= item[0]:
            self.player.hull = Hull(item[0], item[1], item[2])
            self.player.money -= item[0]
            object_game.console(text = 'You have bought: {} hull'.format(item[1]), print = True)

        else:
            system('clear')
            object_game.console(text = 'Need more money', print = True)
