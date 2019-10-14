from pico2d import *
import random


class Ball:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 599
        self.speed = random.randint(2, 6)
        self.type = random.randint(0, 1)
        if self.type == 1:
            self.image = load_image('ball21x21.png')
        elif self.type == 0:
            self.image = load_image('ball41x41.png')

    def update(self):
        self.y -= self.speed

    def draw(self):
        self.image.draw(self.x, self.y)
