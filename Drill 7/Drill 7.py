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


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(0, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False