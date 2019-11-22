from pico2d import *
import random
import game_world
import main_state

class BigBall():
    image = None
    def __init__(self):
        self.x = random.randint(200, 1000)
        self.y = random.randint(300, 900)
        if BigBall.image is None:
            BigBall.image = load_image('ball41x41.png')
        self.hp = 100

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def draw(self):
        BigBall.image.draw(self.x, self.y)

    def update(self):
        pass


class SmallBall():
    image = None

    def __init__(self):
        self.x = random.randint(200, 1000)
        self.y = random.randint(300, 900)
        if SmallBall.image is None:
            SmallBall.image = load_image('ball21x21.png')
        self.hp = 50

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        SmallBall.image.draw(self.x, self.y)

    def update(self):
        pass