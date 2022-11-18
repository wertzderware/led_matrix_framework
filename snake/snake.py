import matrix
from rpi_ws281x import Color

class Snake():
    def __init__(self, time_speed):
        self.position = (7, 7)
        self.color = (Color(255, 255, 0))
        self.segments = [(7, 6), (7, 5)]
        self.speed = 0.3
        self.vel = (0, 1)
        self.time_speed = time_speed
        self.time = 0

    def add_matrix(self, matrix):
        self.matrix = matrix




    def update(self):
        p = self.position
        new_p = (
            p[0] + self.time * self.speed * self.vel[0], 
            p[1] + self.time * self.speed * self.vel[1]
        )
        self.position = new_p
        self.time += self.time_speed

        if not new_p[0] // 1 == p[0] // 1 or not new_p[1] // 1 == p[1] // 1:
            self.shift_segments(p)
        
        if self.position[1] > 22:
            self.position = (self.position[0], 0)
        

    def shift_segments(self, pos):
        self.segments[0] = pos
        self.segments.append(self.segments[0])
        self.segments.pop(0)




    def round_position(self, is_segments=False):
        if is_segments:
            segments = []
            for segment in self.segments:
                segments.append((int(segment[0] // 1), int(segment[1] // 1)))#
            return segments
        else:
            return (int(self.position[0] // 1), int(self.position[1] // 1))

    def draw(self):
        self.matrix.draw_pixel(self.round_position(), Color(255, 0, 255))
        for s in self.round_position(True):
            self.matrix.draw_pixel(s, self.color)
        # extra matrixmethode, die nur einen pixel updatet und den rest nochmal sich selber setzt
