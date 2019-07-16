from termcolor import colored #ON WINDOWS FIRST os.system('color'
import random
import time
from object_game import *

from getch import *
from objects import *
from objects2 import *


map1 = Map()
player1 = Player(map1)
shop1 = Shop(player1)
map1.set_shop(shop1)
game1 = Game(player1, map1)

game1._after_dig()
while(1):
   game1.move()
print("end")
