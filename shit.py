import random
from stuff import Stuff

class Shit(Stuff):
    def __init__(self, game):
        super().__init__('shit.png')
        self.width = 38
        self.height = 38
        self.center_x = random.randint(10, game.width - 10)
        self.center_y = random.randint(10, game.height - 10)
        self.change_x = 0
        self.change_y = 0
        self.score = -1