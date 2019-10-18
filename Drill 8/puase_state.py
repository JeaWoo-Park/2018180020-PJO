from pico2d import *
import main_state
import game_framework


image = load_image('pause.png')


def handle_events():
    if event.type == SDL_QUIT:
        game_framework.quit()
    elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
        game_framework.quit()
    elif event.type == SDL_KEYDOWN and event.key == SDLK_P:
        game_framework.pop_state()

def update():
    image.update()
    pass


def draw():
    clear_canvas()
    image.draw()
    update_canvas()
    pass