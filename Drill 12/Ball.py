from pico2d import *
import random


class Ball:
    image = None
    def __init__(self):
        pass

    def update(self):
        pass




class BigBall(Ball):
    def __init__(self):
        self.x = random.randint(200, 1000)
        self.y = random.randint(300, 900)
        if BigBall.image is None:
            BigBall.image = load_image('ball41x41.png')
        self.hp = 100
    def draw(self):
        BigBall.image.draw(self.x, self.y)

class SmallBall(Ball):
    def __init__(self):
        self.x = random.randint(200, 1000)
        self.y = random.randint(300, 900)
        if SmallBall.image is None:
            SmallBall.image = load_image('ball21x21.png')
        self.hp = 50
    def draw(self):
        SmallBall.image.draw(self.x, self.y)