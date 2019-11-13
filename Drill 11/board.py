from pico2d import *
import game_world
import game_framework


class Board():

    def __init__(self):
        self.SPEED = 80
        self.image = load_image("brick180x40.png")
        self.x, self.y = 300, 200

    def get_bb(self):
        return self.x - 90, self.y - 20, self.x + 90, self.y + 20

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.x += self.SPEED * game_framework.frame_time
        if self.x > 1600 - 90:
            self.SPEED *= -1
        elif self.x < 90:
            self.SPEED *= -1
