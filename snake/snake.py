from rpi_ws281x import Color
from game_object import Game_object

class Snake(Game_object):

    def __init__(self, time):
        super().__init__(time=time, pos=(7, 7), vel=(0, 1), speed=0.5)
        self.color = (Color(50, 255, 50))
        self.segments = [(7, 6), (7, 5)]
        self.extend_elements = 0

    def update(self):

        p = self.pos
        # print('snake.update() -> speed: ', self.speed, ' | vel: ', self.vel)
        p_new = (
            p[0] + self.speed * self.vel[0], 
            p[1] + self.speed * self.vel[1]
        )

        if not p_new[0] // 1 == p[0] // 1 or not p_new[1] // 1 == p[1] // 1:
            if self.extend_elements:
                self.segments.append(self.round_position())
                self.extend_elements -= 1
            else:
                self.shift_segments(p)
        
        self.pos = p_new
        
        # overflow after breaching border
        x = self.canvas.width
        y = self.canvas.height
        if self.pos[1] >= y:
            self.pos = (self.pos[0], 0)
        elif self.pos[1] <= 0:
            self.pos = (self.pos[0], y - 1 + self.pos[1])
        elif self.pos[0] >= x:
            self.pos = (0, self.pos[1])
        elif self.pos[0] <= 0:
            self.pos = (x - 1 + self.pos[0], self.pos[1])
        

    def shift_segments(self, pos):
        self.segments[0] = pos
        self.segments.append(self.segments.pop(0))

    def extend(self, amount=1):
        self.extend_elements = amount

    def turn(self, direction='up'):
        # print('turn: ', direction, ' | ', self.pos, ' | ', self.round_position())
        if direction == 'up' and not self.vel == (0, -1):
                self.vel = (0, 1)
        elif direction == 'down' and not self.vel == (0, 1):
                self.vel = (0, -1)
        elif direction == 'right' and not self.vel == (-1, 0):
                self.vel = (1, 0)
        elif direction == 'left' and not self.vel == (1, 0):
                self.vel = (-1, 0)

    def draw(self):
        self.canvas.matrix.draw_pixel(self.round_position(), self.color)
        for s in self.round_position(True):
            self.canvas.matrix.draw_pixel(s, Color(0, 255, 0))
