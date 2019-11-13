import game_framework
from pico2d import *

import game_world

PIXEL_PER_METER = (10.0 / 3.0)
RUN_SPEED_KMPH = 20
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class RIGHT_FlyState:

    @staticmethod
    def enter():
        pass

    @staticmethod
    def exit():
        pass

    @staticmethod
    def do(bird):
        bird.frame = (bird.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        bird.x += bird.velocity * game_framework.frame_time
        bird.x = clamp(25, bird.x, 1600 - 25)

    @staticmethod
    def draw(bird):
        if bird.dir == 1:
            bird.image.clip_draw(int(bird.frame) * 100, 100, 100, 100, bird.x, bird.y)
        else:
            bird.image.clip_draw(int(bird.frame) * 100, 0, 100, 100, bird.x, bird.y)


class Left_FlyState:

    @staticmethod
    def enter():
        pass

    @staticmethod
    def exit():
        pass

    @staticmethod
    def do(bird):
        bird.frame = (bird.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        bird.x -= bird.velocity * game_framework.frame_time
        bird.x = clamp(25, bird.x, 1600 - 25)

    @staticmethod
    def draw(bird):
        if bird.dir == 1:
            bird.image.clip_draw(int(bird.frame) * 100, 100, 100, 100, bird.x, bird.y)
        else:
            bird.image.clip_draw(int(bird.frame) * 100, 0, 100, 100, bird.x, bird.y)


class Bird:

    def __init__(self):
        self.x, self.y = 1600 // 2, 400
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('bird_animation.png')
        self.dir = 1
        self.velocity = 200
        self.frame = 0
        self.event_que = []
        self.cur_state = RIGHT_FlyState
        self.cur_state.enter()

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if self.x < 0:
            self.cur_state.exit()
            self.cur_state = RIGHT_FlyState
            self.cur_state.enter()
        if self.x > 1600:
            self.cur_state.exit()
            self.cur_state = Left_FlyState
            self.cur_state.enter()



    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        pass
