from canvas import Canvas
from time import sleep
from shape import Shape

# upgrades/food should be pulsating in rainbpow





class Game():

    def __init__(self):

        self.field = (13, 19)
        self.canvas = Canvas(self.field)
        self.speed = 0.001
        self.running = True
        self._time = 0
        self.score = 0

        self.objects = []

        self.rows = []
        for i in range(len(self.field[1])):
            self.rows.append([0] * len(self.field(0)))


        for o in self.objects:
            self.canvas.ad_object(o)


        self.canvas.draw()




#========================= MAIN LOOP ========================
    def start(self):
        while self.running:

            self.update()
            self.canvas.draw()
            # self.check_input()

            sleep(self.speed)
            self._time += self.speed


    def check_rows(self):
        rows_completed = 0
        for i, row in enumerate(self.rows):
            if self.check_row(row):
                rows_completed += 1
                self.rows.pop(i)
                self.rows.append([0] * self.field[1])
        if rows_completed > 0:
            self.score += pow(2, rows_completed) * self.field[1] 


    def check_row(self, index):
        result = 1
        for i in self.rows[index]:
            result *= i
        return result



    def time(self):
        return self._time

    def check_input(self):
        self

    def update(self):

        self.check_rows()

        for o in self.objects:
            o.update()





game = Game()
game.start()
