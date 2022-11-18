import matrix


# test if brightness can be set per pixel
# then an overall brightness can be defined
# single pixel brightness = overall brightness / percentage

class Canvas():
    def __init__(self, width=13, height=23):
        self.matrix = matrix.Matrix(width, height)
        self.objects = []

    def update(self):
        self.matrix.clear()
        for o in self.objects:
            o.draw()
        self.matrix.pixels.show()

    def ad_object(self, obj):
        self.objects.append(obj)
        obj.add_matrix(self.matrix)
