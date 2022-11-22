from rpi_ws281x import Color
# import matrix

class Organism():

    def __init__(self, canvas, organisms, pos=False):

        self.matrix = canvas.matrix
        self.pos = pos or self.matrix.random_point()
        self.organisms = organisms
        self.status = 'dead'
        self.neighbours = []

    
    def draw(self):

        color = Color(0, 0, 0)

        if self.status == 'alive':
            color = Color(0, 255 ,0)
        if self.status == 'spawning':
            color = Color(0, 255 ,255)
        if self.status == 'dead':
            color = Color(255, 0 ,0)

        self.matrix.draw_pixel(self.pos, color)

    def update(self):

        neighbours = self.alive_neighbours()
        if neighbours > 0:
            print('\n Organism ', self.pos)
            for n in self.neighbours:
                print(n.pos, end=', ')

        if neighbours == 3:
            self.status = 'spawning'
        if neighbours < 2 or neighbours > 3:
            self.status = 'dying'

    def add_neighbours(self):

        n = self.pos[1] < self.matrix.height - 1
        e = self.pos[0] < self.matrix.width - 1
        s = self.pos[1] > 0
        w = self.pos[0] > 0

        #diagonals as well
        if n:
            self.neighbours.append(self.organisms[self.matrix.pixel_indeces[self.pos[0]][self.pos[1] + 1]])
            if e:
                self.neighbours.append(self.organisms[self.matrix.pixel_indeces[self.pos[0] + 1][self.pos[1] + 1]])
            if w:
                self.neighbours.append(self.organisms[self.matrix.pixel_indeces[self.pos[0] - 1][self.pos[1] + 1]])
        if e:
            self.neighbours.append(self.organisms[self.matrix.pixel_indeces[self.pos[0] + 1][self.pos[1]]])
            # if n:
            #     self.neighbours.append(self.organisms[self.matrix.pixel_indeces[self.pos[0] + 1][self.pos[1] + 1]])
            # if s:
            #     self.neighbours.append(self.organisms[self.matrix.pixel_indeces[self.pos[0] + 1][self.pos[1] - 1]])
        if s:
            self.neighbours.append(self.organisms[self.matrix.pixel_indeces[self.pos[0]][self.pos[1] - 1]])
            if e:
                self.neighbours.append(self.organisms[self.matrix.pixel_indeces[self.pos[0] + 1][self.pos[1] - 1]])
            if w:
                self.neighbours.append(self.organisms[self.matrix.pixel_indeces[self.pos[0] - 1][self.pos[1] - 1]])
        if w:
            self.neighbours.append(self.organisms[self.matrix.pixel_indeces[self.pos[0] - 1][self.pos[1]]])
            # if n:
            #     self.neighbours.append(self.organisms[self.matrix.pixel_indeces[self.pos[0] - 1][self.pos[1] + 1]])
            # if s:
            #     self.neighbours.append(self.organisms[self.matrix.pixel_indeces[self.pos[0] - 1][self.pos[1] - 1]])


    def alive_neighbours(self, status=['alive']):

        amount = 0

        for n in self.neighbours:
            amount += n.status in status

        return amount