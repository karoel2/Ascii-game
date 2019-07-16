from getch import *


def menu():
    print('1. Sell all')
    print('2. Refill')
    print('3. Buy upgrades')
    print('0. Return')
    char = getch().lower()
    if char == 3:
        buy_upgrades()
    else:
        menu()

def buy_upgrades():
    print('1. Buy fuel_tank')
    print('2. Buy cargo_bay')
    print('3. Buy engine')
    print('4. Buy drill')
    print('5. Buy hull')
    print('0. Return')
    char = getch().lower()
    if char == 1:
        printy('fuel_tank')
    elif char == 2:
        printy('cargo_bay')
    elif char == 3:
        printy('engine')
    elif char == 4:
        printy('drill')
    elif char == 5:
        printy('hull')
    elif char == 0:
        menu()
    else:
        buy_upgrades()

def printy(thing):

    print('1. Buy reinforced {} 100$'.format(thing))
    print('2. Buy improved {} 1000$'.format(thing))
    print('3. Buy advanced {} 5000$'.format(thing))
    print('4. Buy military class 20000$ {}'.format(thing))
    print('0. Return')
    char = getch().lower()
    print(char)
    if char == 0:
        buy_upgrades()
    elif char in range(4):
        buy_fuel_tank(char)
    else:
        printy(thing)

def buy_fuel_tank(quality):
    list = [
    [100, 'reinforced', 40],
    [1000, 'improved', 75],
    [5000, 'advanced', 100],
    [20000, 'military class', 200]
    ]
    item = list[quality - 1]

def buy_cargo_bay(quality):
    list = [
    [100, 'reinforced', 20],
    [1000, 'improved', 35],
    [5000, 'advanced', 55],
    [20000, 'military class', 100]
    ]
    item = list[quality - 1]

def buy_engine(quality):
    list = [
    [100, 'reinforced', 1.25],
    [1000, 'improved', 1.60],
    [5000, 'advanced', 2.0],
    [20000, 'military class', 2.75]
    ]
    item = list[quality - 1]

def buy_drill(quality):
    list = [
    [100, 'reinforced', 1.25],
    [1000, 'improved', 1.60],
    [5000, 'advanced', 2.0],
    [20000, 'military class', 2.75]
    ]
    item = list[quality - 1]

def buy_hull(quality):
    list = [
    [100, 'reinforced', 8],
    [1000, 'improved', 14],
    [5000, 'advanced', 22],
    [20000, 'military class', 40]
    ]
    item = list[quality - 1]
