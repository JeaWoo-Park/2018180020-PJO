import random
import json
import pickle
import os

import world_build_state
import game_framework
from pico2d import *

font = None


def enter():
    global font
    font = load_font('ENCR10B.TTF', 20)


def exit():
    pass


def pause():
    pass


def resume():
    pass


def update():
    pass


def draw():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(world_build_state)
