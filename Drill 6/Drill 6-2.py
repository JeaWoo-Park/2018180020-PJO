from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024




def handle():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


running = True
k_x, k_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
open_canvas(KPU_WIDTH, KPU_HEIGHT)
Kpu = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hide_cursor()
while running:
    clear_canvas()
    Kpu.draw(k_x, k_y)
    update_canvas()
    handle()
close_canvas()
