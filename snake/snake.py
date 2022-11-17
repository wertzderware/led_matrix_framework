import matrix
from rpi_ws281x import Color

class Snake():
    def __init__(self):
        self.position = (7, 7)
        self.color = (Color(255, 255, 0))
        self.segments = [(7, 6), (7, 5)] 

    def add_matrix(self, matrix):
        self.matrix = matrix

    def draw(self):
        #!!!!!!!!!!!!!!!!!andere color für kopf
        self.matrix.draw_pixel(self.position, Color(255, 0, 255))
        for s in self.segments:
            self.matrix.draw_pixel(s, self.color)
        self.matrix.pixels.show()
            # extra matrixmethode, die nur einen pixel updatet und den rest nochmal sich selber setzt
