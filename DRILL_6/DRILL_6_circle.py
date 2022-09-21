from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

cycle = 0
degree = 0
r = 230

# 중점을 400, 300으로

while True:
    
    xpos = 400 + r*math.cos(degree)
    ypos = 300 + r*math.sin(degree)
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(xpos, ypos)
    
    degree += 0.2

    delay(0.1)
