import matrix
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


# test if brightness can be set per pixel
# then an overall brightness can be defined
# single pixel brightness = overall brightness / percentage

class Canvas():
    def __init__(self, width=13, height=23):
        self.matrix = matrix.Matrix(width, height, 10)
        self.objects = []
 
    def draw(self):
        self.matrix.clear()
        for o in self.objects:
            o.draw()
        self.matrix.pixels.show()

    def ad_object(self, obj):
        self.objects.append(obj)
