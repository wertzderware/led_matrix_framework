from snake import Snake
from canvas import Canvas
from time import sleep

# upgrades/foo should be pulsating in rainbpow


class Game():

    def __init__(self):

        self.canvas = Canvas()
        self.speed = 0.01
        self.running = True
        self.time = 0

        self.objects = [Snake(self.speed)]

        for o in self.objects:
            self.canvas.ad_object(o)

        self.canvas.update()

#========================= MAIN LOOP ========================
    def start(self):
        while self.running:
            self.update()
            self.canvas.update()
            sleep(self.speed)
            self.time += self.speed



    def update(self):
        for o in self.objects:
            o.update()


game = Game()
game.start()