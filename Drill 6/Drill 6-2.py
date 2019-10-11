from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def stop():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def move_3points(p1, p2, p3):
    global frame
    for i in range(500, 1000, 2):
        frame = (frame + 1) % 8
        t = i / 1000
        x = (2 * t ** 2 - 3 * t + 1) * p1[0] + (-4 * t ** 2 + 4 * t) * p2[0] + (2 * t ** 2 - t) * p3[0]
        y = (2 * t ** 2 - 3 * t + 1) * p1[1] + (-4 * t ** 2 + 4 * t) * p2[1] + (2 * t ** 2 - t) * p3[1]
        clear_canvas()
        Kpu.draw(k_x, k_y)
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        update_canvas()
        stop()


def move_4point(p1, p2, p3, p4):
    global frame
    # draw p1-p2
    for i in range(0, 1000, 2):
        frame = (frame + 1) % 8
        t = i / 1000
        x = ((-t ** 3 + 2 * t ** 2 - t) * p4[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p1[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p2[0] + (t ** 3 - t ** 2) * p3[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p4[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p1[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p2[1] + (t ** 3 - t ** 2) * p3[1]) / 2
        clear_canvas()
        Kpu.draw(k_x, k_y)
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        update_canvas()
        stop()
    # draw p2-p3
    for i in range(0, 1000, 2):
        frame = (frame + 1) % 8
        t = i / 1000
        x = ((-t ** 3 + 2 * t ** 2 - t) * p1[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p3[0] + (t ** 3 - t ** 2) * p4[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p1[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p3[1] + (t ** 3 - t ** 2) * p4[1]) / 2
        clear_canvas()
        Kpu.draw(k_x, k_y)
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        update_canvas()
        stop()
    # draw p3-p4
    for i in range(0, 1000, 2):
        frame = (frame + 1) % 8
        t = i / 1000
        x = ((-t ** 3 + 2 * t ** 2 - t) * p2[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p3[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p4[0] + (t ** 3 - t ** 2) * p1[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p2[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p3[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p4[1] + (t ** 3 - t ** 2) * p1[1]) / 2
        clear_canvas()
        Kpu.draw(k_x, k_y)
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        update_canvas()
        stop()


def move(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10):
    move_4point(p1, p2, p3, p4)
    move_4point(p4, p5, p6, p7)
    move_4point(p7, p8, p9, p10)
    move_3points(p9, p10, p1)


size = 10
points = [(random.randint(0, 1280), random.randint(300,700)) for i in range(size)]
frame = 0
running = True
k_x, k_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
open_canvas(KPU_WIDTH, KPU_HEIGHT)
Kpu = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hide_cursor()
while running:
    move(points[0], points[1], points[2], points[3], points[4], points[5], points[6], points[7], points[8], points[9])
close_canvas()
