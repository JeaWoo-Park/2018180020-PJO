from pico2d import *

KPU_W, KPU_H = 1280, 1024

x, y = KPU_W, KPU_H
running = True


def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_H - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas(KPU_W, KPU_H)
kpu_ground = load_image('KPU_GROUND.png')
mouse = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')
frame = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_W // 2, KPU_H // 2)

    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()
