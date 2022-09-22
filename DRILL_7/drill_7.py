from pico2d import *

open_canvas()

cygnus = load_image('cignus_attack_2.png')

# 38
# 19

frame = 0
yframe = 0
while True:
    clear_canvas()
    cygnus.clip_draw(frame * 380, yframe, 380, 490, 400, 300)
    update_canvas()
    frame = (frame + 1) % 19
    if (frame == 18 and yframe == 0):
        yframe = 1
    elif (frame == 18 and yframe == 1):
        yframe = 0
    delay(0.1)
    get_events()

close_canvas()