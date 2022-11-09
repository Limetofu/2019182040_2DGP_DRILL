from pico2d import *
import game_world
import game_framework

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = RUN_SPEED_KMPH * 1000.0 / 60.0
RUN_SPEED_MPS = RUN_SPEED_MPM / 60.0
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

bird_w = 0
bird_h = 0

class Bird:
    image = None

    def __init__(self, x = 400, y = 600, velocity = 1):
        self.x, self.y = x, y
        self.frame = 0
        self.dir = 0
        if Bird.image == None:
            self.image = load_image('bird_animation.png')
            global bird_w, bird_h
            bird_w, bird_h = self.image.w, self.image.h

        self.font = load_font('ENCR10B.TTF', 16) # 폰트 이름, 사이즈

        self.yframe = 0

    def update(self):
        if self.frame == 4:
            if self.yframe <= 1:
                self.yframe += 1
            else:
                self.yframe = 0

        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5

        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time

        self.x = clamp(20, self.x, 1600 - 25)

    def draw(self):
        if self.x >= 1580: # 넘어가면
            self.dir = -1
        elif 20 >= self.x:
            self.dir = 1

        yvalue = bird_h // 3
        wvalue = bird_w // 5

        if self.dir == -1:
            self.image.clip_composite_draw(int(self.frame) * int(wvalue), int(self.yframe) * int(yvalue), 100, 100, 
                                            0, 'v', self.x, self.y, 100, 100)
        elif self.dir == 1:
            self.image.clip_composite_draw(int(self.frame) * int(wvalue), int(self.yframe) * int(yvalue), 100, 100, 
                                            0, '', self.x, self.y, 100, 100)

        self.font.draw(self.x - 60, self.y + 50, f'({get_time():.2f})', (255, 255, 0))