from pico2d import *
import main_state
import game_framework

time = 0.0


class puase:
    def __init__(self):
        self.image = load_image('pause.png')
        self.timer = True
    def draw(self):
        if self.timer == True:
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
    global time
    if time > 0.5:
        time = 0
        if image.timer == False:
            image.timer = True
        elif image.timer == True:
            image.timer = False
    delay(0.01)
    time += 0.01
    pass


def draw():
    clear_canvas()
    game_framework.stack[-2].draw()
    image.draw()
    update_canvas()
    pass
