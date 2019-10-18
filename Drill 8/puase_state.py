from pico2d import *
import main_state
import game_framework


class puase:
    def __init__(self):
        self.image = load_image('pause.png')

    def draw(self):
        self.image.draw(400, 300, 200, 200)


def exit():
    global image
    del image


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_state()


def enter():
    global image
    image = puase()


def update():
    pass


def draw():
    clear_canvas()
    image.draw()
    update_canvas()
    pass
