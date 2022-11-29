from snake import Snake
from canvas import Canvas
from time import sleep
from algorythm import Algorythm
from food import Food

# upgrades/food should be pulsating in rainbpow


class Game():

    def __init__(self):

        self.canvas = Canvas()
        self.speed = 0.001
        self.running = True
        self._time = 0

        self.snake = Snake(self.time)
        self.foods = [Food(self.time)]
        self.objects = [self.snake, *self.foods]

        self.algorythm = Algorythm(self.objects[0])

        for o in self.objects:
            self.canvas.ad_object(o)

        self.canvas.draw()




#========================= MAIN LOOP ========================
    def start(self):
        while self.running:

            self.update()
            self.algorythm.update()
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

        for f in self.foods:
            if self.snake.intersect(f):
                self.snake.extend()
                f.spawn_new()




game = Game()
game.start()
