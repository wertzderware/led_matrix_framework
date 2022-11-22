from canvas import Canvas
from time import sleep
from organism import Organism




class Game():

    def __init__(self):

        self.canvas = Canvas()
        self.speed = 0.3
        self.running = True
        self._time = 0
        self.organisms = []

        # make it go after the pixel_indeces from matrix and copy that
        # for x in range(self.canvas.matrix.width):
        for x, p in enumerate(self.canvas.matrix.pixel_indeces):
            # for y in range(self.canvas.matrix.height):
            for y, p2 in enumerate(p):
                o = Organism(self.canvas, self.organisms, (x, y))
                self.organisms.append(o)
                self.canvas.ad_object(o)

        for o in self.organisms:
            o.add_neighbours()

        for i in range(100):
            p = self.canvas.matrix.random_point()
            index = self.canvas.matrix.pixel_indeces[p[0]][p[1]]
            self.organisms[index].status = 'alive'
            # for o in self.organisms:
            #     if o.pos == p:
            #         o.status = 'alive'
                    

        # self.canvas.draw()

#========================= MAIN LOOP ========================
    def start(self):
        while self.running:

            self.update()
            self.canvas.draw()

            sleep(self.speed)
            self._time += self.speed

            input()







    def time(self):
        return self._time

    def check_input(self):
        self

    def update(self):
        for o in self.organisms:
            o.update()

game = Game()
game.start()