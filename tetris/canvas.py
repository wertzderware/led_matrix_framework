import random
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from matrix import Matrix


# test if brightness can be set per pixel
# then an overall brightness can be defined
# single pixel brightness = overall brightness / percentage

class Canvas():
    def __init__(self, field=(0, 0), width=13, height=23):
        self.matrix = Matrix(width, height, 25)
        self.objects = []
        self.width = field[0]
        self.height = field[1]
        self.info = ''




    def draw(self):
        self.matrix.clear()
        self.matrix.text(self.info, (1, 19))
        for o in self.objects:
            o.draw()
        self.matrix.pixels.show()

    def set_info(self, info):
        self.info = info

    def ad_object(self, obj):
        self.objects.append(obj)
        obj.add_canvas(self)

    # def random_point(self):
    #     return (random.randint(0, self.width - 1), random.randint(0, self.height - 1))
