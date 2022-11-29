from rpi_ws281x import Color
from game_object import Game_object


class Food(Game_object):
    def __init__(self, time):
        super().__init__(pos=(-1, -1), time=time)

    def draw(self):
        self.matrix.draw_pixel(self.round_position(), Color(0, 0, int((self.time() * 10000 % 255 / 2))))


    def add_matrix(self, matrix):
        super().add_matrix(matrix)
        self.pos = (7, 9)
        # self.spawn_new()

    def spawn_new(self):
        self.pos = self.matrix.random_point()
        