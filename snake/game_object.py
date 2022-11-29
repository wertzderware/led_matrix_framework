

class Game_object():

    def __init__(self, pos, time=0, speed=0, vel=(0, 0)):
        self.time = time
        self.pos = pos
        self.speed = speed
        self.vel = vel
    
    def update(self):
        self

    def round_position(self, is_segments=False):
        if is_segments:
            segments = []
            for segment in self.segments:
                segments.append((int(segment[0] // 1), int(segment[1] // 1)))
            return segments
        else:
            return (int(self.pos[0] // 1), int(self.pos[1] // 1))

    def add_matrix(self, matrix):
        self.matrix = matrix

    def intersect(self, obj):
        return self.round_position() == obj.round_position()