from termcolor import colored #ON WINDOWS FIRST os.system('color'
from getch import *


class Upgrade():
    def __init__(self, cost, name):
        self.cost = cost
        self.name = name

class Fuel_Tank(Upgrade):

    def __init__(self, cost, name, size):
        super().__init__(cost, name)
        self.fuel_amount = size
        self.size = size

    def loss(self, amount):
        self.fuel_amount -= amount

    def refill(self):
        temp = self.size - self.fuel_amount
        self.fuel_amount = self.size
        return temp

    def print_fuel(self):
        fuel = self.fuel_amount/self.size
        temp = []
        temp.append(colored('[', 'yellow'))
        for item in range(int(16 * fuel)):
            temp.append(colored('█', 'yellow'))
        for item in range(16 - int(16 * fuel)):
            temp.append(colored('█', 'grey'))
        temp.append(colored(']', 'yellow'))
        return temp

class Cargo_Bay(Upgrade):
    item_list = []
    def __init__(self, cost, name, size):
        super().__init__(cost, name)
        self.size = size

    def add(self, item):
        if len(self.item_list) < self.size:
                self.item_list.append(item)
        else:
            console(text = 'Inventory is full!')


class Engine(Upgrade):

    def __init__(self, cost, name, speed):
        super().__init__(cost, name)
        self.speed = speed

class Drill(Upgrade):

    def __init__(self, cost, name, effecitvity):
        super().__init__(cost, name)
        self.effecitvity = effecitvity

class Hull(Upgrade):

    def __init__(self, cost, name, durability_max):
        super().__init__(cost, name)
        self.durability_max = durability_max
        self.durability_left = durability_max

    def dmg(self, amount):
        self.durability_left -= amount
        self.death

    def death(self):
        if self.durability_left <= 0:
            clear()
            print("GAME OVER")
            return False
        else:
            return True


    def print_hull(self):
        hull = self.durability_left/self.durability_max
        temp = []
        temp.append(colored('[', 'red'))
        for item in range(int(16 * hull)):
            temp.append(colored('█', 'red'))
        for item in range(16 - int(16 * hull)):
            temp.append(colored('█', 'grey'))
        temp.append(colored(']', 'red'))
        return temp
