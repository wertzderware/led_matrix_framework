from snake import Snake
from canvas import Canvas
from time import sleep


# upgrades/food should be pulsating in rainbpow


class Game():

    def __init__(self):

        self.canvas = Canvas()
        self.speed = 0.01
        self.running = True
        self._time = 0
        self.objects = [Snake(self.time)]

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

    def time(self):
        return self._time

    def check_input(self):
        self

    def update(self):
        for o in self.objects:
            o.update()

game = Game()
game.start()