from pico2d import *


def handle_events():
    global running
    global y
    global dir
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                y = 1
                dir += 1
            elif event.key == SDLK_LEFT:
                y = 0
                dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                y = 3
                dir -= 1
            elif event.key == SDLK_LEFT:
                y = 2
                dir += 1

    pass


open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')
running = True
frame = 0
dir = 0
x = 400
y = 2

while running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 100 * y, 100, 100, x, 90)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    if 780 > x + dir * 5 > 20:
        x += dir * 5
    delay(0.005)

close_canvas()
