import random
from time import sleep
from rpi_ws281x import PixelStrip, Color

colors = [ 
    Color(255, 0, 0), # red
    Color(255, 10, 0), 
    Color(255, 25, 0), 
    Color(255, 165, 0), 
    Color(255, 195, 0),
    Color(255, 225, 0),
    Color(255, 255, 0),
    Color(170, 213, 0),
    Color(50, 200, 0),
    Color(0, 170, 0), # green
    Color(0, 85, 85),
    Color(0, 43, 170),
    Color(0, 0, 255), # blue
    Color(25, 0, 213),
    Color(50, 0, 172),
    Color(75, 0, 130),
    Color(129, 43, 166),
    Color(184, 87, 202),
    Color(255, 20, 20)
]

class Matrix():
    def __init__(self, width, height, brightness=100):
        self.width = width
        self.height = height
        self.amount_pixels = width * height
        self.pixels = PixelStrip(self.amount_pixels, 18, 800000, 10, False, brightness, 0)
        self.pixel_indeces = []
        self.pixels.begin()

        # init pixels in 2D array - data line from bottomright to topleft
        for x in range(width):
            self.pixel_indeces.append([])
            for y in range(height):
                if x % 2 == 1:
                    index = self.amount_pixels - (height * x) - (y + 1)
                else:
                    index = self.amount_pixels - (height * (x + 1)) + y
                self.pixel_indeces[x].append(index)

    def scroll_shape(self, shapes, colors, speed=0.05):
        #scrolling one shape with height as distance works perfect - otherwise really janky
        frame = 0
        distance = 23
        
        while True:
            self.clear()
            for shape_index, shape in enumerate(shapes):
                y = (frame ) - (distance * shape_index)
                if y + len(shape) > self.height:
                    self.draw_shape(shape, (1, y), colors[shape_index], True)
                else:
                    self.draw_shape(shape, (1, y), colors[shape_index])
            sleep(speed)
            frame += 1
            self.pixels.show()

    def draw_shape(self, shape, position, color, overflow=False):
        # start in bottom left corner shape is an array of 0 / 1

        _shape = []
        for i in range(len(shape)):
            _shape.append(shape[len(shape) - 1 - i])

        for i, col in enumerate(_shape):
            if (position[1] + i >= self.height and not overflow) or position[1] + i < 0: continue
            for j, v in enumerate(col):
                if (j + position[0] >= self.width and not overflow) or j + position[0] < 0: break
                if v == '1':
                    self.draw_pixel(((position[0] + j) % self.width, (position[1] + i) % self.height), color)

    def test_colors(self):
        self.draw_rectangle((0, 0), (self.width - 1, self.height - 1), Color(255, 255, 255))
        self.draw_rectangle((1, 1), (self.width - 2, self.height - 2), Color(255, 255, 255))
        shift = 0
        while True:
            for i in range(len(colors)):
                y = (i + shift) % len(colors) + 2
                self.draw_line((2, y), (self.width - 3, y), colors[i % len(colors)])
            self.pixels.show()
            shift += 1
            sleep(0.001)

    def test(self):
        for x in range(self.width):
            for y in range(self.height):
                print('(X/Y) -> (', x, '/', y, ') -> ', self.pixel_indeces[x][y])
                self.pixels.setPixelColor(self.pixel_indeces[x][y], (255, 255, 255))
                self.pixels.show()
                sleep(0.1)

    def draw_line(self, p1, p2, color):
        if p1[0] == p2[0]:
            x = p1[0]
            y_min = p1[1] if p1[1] < p2[1] else p2[1]
            y_max = p1[1] if p1[1] > p2[1] else p2[1]
            for y in range(y_max + 1 - y_min):
                self.pixels.setPixelColor(self.pixel_indeces[x][y + y_min], color)
        elif p1[1] == p2[1]:
            y = p1[1]
            x_min = p1[0] if p1[0] < p2[0] else p2[0]
            x_max = p1[0] if p1[0] > p2[0] else p2[0]
            for x in range(x_max + 1 - x_min):
                self.pixels.setPixelColor(self.pixel_indeces[x + x_min][y], color)
                
    def clear(self, update=False):
        for i in range(self.amount_pixels):
            self.pixels.setPixelColor(i, Color(0, 0, 0))
        if update:
            self.pixels.show()
     
    def draw_pixel(self, pos_new, color_new, pos_old=False, color_old=Color(0, 0, 0)):
        if pos_old:
            self.pixels.setPixelColor(self.pixel_indeces[pos_old[0]][pos_old[1]], color_old)
        else:
            self.pixels.setPixelColor(self.pixel_indeces[pos_new[0]][pos_new[1]], color_new)
            
    def draw_rectangle(self, p1, p2, color):
        self.draw_line(p1, (p1[0], p2[1]), color)
        self.draw_line(p1, (p2[0], p1[1]), color)
        self.draw_line(p2, (p1[0], p2[1]), color)
        self.draw_line(p2, (p2[0], p1[1]), color)

    def random_point(self):
        return (random.randint(0, self.width - 1), random.randint(0, self.height - 1))


