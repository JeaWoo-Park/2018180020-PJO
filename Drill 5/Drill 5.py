from pico2d import *

KPU_W, KPU_H = 1280, 1024

x, y = KPU_W, KPU_H
running = True
char_point = [500, 500]



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
        elif event.type == SDL_MOUSEBUTTONDOWN and event.key == SDL_BUTTON_LEFT:
            p2 = [event.x, event.y]
            p1 = char_point
            move_character(p1, p2)


def move_character(p1, p2):
    global frame
    for i in range(0, 100 + 1, 5):
        t = i / 100
        x1 = (1 - t) * p1[0] + t * p2[0]
        y1 = (1 - t) * p1[1] + t * p2[1]
    e = get_events()
    frame = (frame + 1) % 8


frame = 0

char_state = 0  # 0 왼쪽 달림 2 오른쪽 달림 3 왼쪽 멈춤 4 오른쪽 멈춤
open_canvas(KPU_W, KPU_H)
kpu_ground = load_image('KPU_GROUND.png')
mouse = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')

hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_W // 2, KPU_H // 2)
    mouse.draw(x + 20, y - 22)

    character.clip_draw(frame * 100, 100 * char_state, 100, 100, char_point[0], char_point[1])
    handle_events()
    frame = (frame + 1) % 8

    update_canvas()
close_canvas()
