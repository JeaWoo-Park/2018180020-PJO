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
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            p2 = [event.x, KPU_H - 1 - event.y]
            p1 = char_point
            move_character(p1, p2)


frame = 0
char_state = 3  # 0 왼쪽 달림 1 오른쪽 달림 2 왼쪽 멈춤 3 오른쪽 멈춤


def move_character(p1, p2):
    global frame
    global char_state
    if p1[0] > p2[0]:
        char_state = 0
    elif p1[0] < p2[0]:
        char_state = 1
    for i in range(0, 50 + 1, 2):
        clear_canvas()
        kpu_ground.draw(KPU_W // 2, KPU_H // 2)
        mouse.draw(x + 20, y - 22)
        t = i / 50
        x1 = (1 - t) * p1[0] + t * p2[0]
        y1 = (1 - t) * p1[1] + t * p2[1]
        char_point[0] = x1
        char_point[1] = y1
        character.clip_draw(frame * 100, 100 * char_state, 100, 100, char_point[0], char_point[1])
        frame = (frame + 1) % 8
        update_canvas()
        delay(0.01)
    char_state += 2


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
