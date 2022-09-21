from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
y = 90 # y 기본값 90

heading_right = 1
heading_up = 0
heading_left = 0
heading_down = 0

cycle = 0

while True:
    clear_canvas_now()
    grass.draw_now(400, 30)
    # 여기까지 고정 
    character.draw_now(x, y)
    
    if heading_right == 1:
        if (x + 42 > 800): # 오른쪽 끝
            heading_right = 0
            heading_up = 1
        x += 5
            
    if heading_up == 1:
        if (y + 92 > 600):
            heading_left = 1
            heading_up = 0
        y += 5
        
    if heading_left == 1:
        if (x - 42 < 0):
            heading_left = 0
            heading_down = 1
        x -= 5
        
    if heading_down == 1:
        if (y - 92 < 0):
            heading_down = 0
            heading_right = 1
            cycle += 1
        y -= 5

    delay(0.01)

    if cycle == 3:
        close_canvas()
