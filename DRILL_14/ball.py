import server

from pico2d import *
from random import randint
import game_world

class Ball:
    image = None

    def __init__(self):
        self.image = load_image('ball21x21.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h

        self.x = randint(0, 1837)
        self.y = randint(0, 1109)


        pass

    def draw(self):
        self.image.draw(self.x - self.window_left, self.y - self.window_bottom, 
                        self.w, self.h)
        pass

    def update(self):
        self.window_left = clamp(0,
                                 int(server.boy.x) - self.canvas_width // 2,
                                 self.canvas_width - 1)
        self.window_bottom = clamp(0, 
                                    int(server.boy.y) - self.canvas_height // 2,
                                    self.canvas_height - 1)                     

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, other, group):
        if group == 'boy:ball':
            game_world.remove_object(self)