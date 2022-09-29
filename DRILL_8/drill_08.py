from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global running
    global dir, ydir, w_anime
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
                w_anime = 1
            elif event.key == SDLK_LEFT:
                dir -= 1
                w_anime = 0
            elif event.key == SDLK_UP:
                ydir += 1
                if (w_anime == 3):
                    w_anime = 1
                elif (w_anime == 2):
                    w_anime = 0
            elif event.key == SDLK_DOWN:
                ydir -= 1
                if (w_anime == 3):
                    w_anime = 1
                elif (w_anime == 2):
                    w_anime = 0

            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
                w_anime = 3
            elif event.key == SDLK_LEFT:
                dir += 1
                w_anime = 2
            elif event.key == SDLK_UP:
                ydir -= 1
                if (w_anime == 1):
                    w_anime = 3
                elif (w_anime == 0):
                    w_anime = 2
            elif event.key == SDLK_DOWN:
                ydir += 1
                if (w_anime == 1):
                    w_anime = 3
                elif (w_anime == 0):
                    w_anime = 2

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
dir = 0
ydir = 0
w_anime = 3

# w_anime == 0 왼쪽 뜀

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * w_anime, 100, 100, x, y)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8

    if (0 < x + dir * 5 and x + dir * 5 < KPU_WIDTH):
        x += dir * 5
    if (0 < y + ydir * 3 and y + ydir * 3 < KPU_HEIGHT):
        y += ydir * 3

close_canvas()

