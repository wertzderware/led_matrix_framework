from snake import Snake
import random

class Algorythm():
    def __init__(self, snake):
        self.snake = snake
        self.updates = 1

    def update(self):
        if self.updates % [5, 10, 20][random.randint(0, 2)] == 0:
            self.snake.turn(['up', 'right', 'down', 'left'][random.randint(0, 3)])
        self.updates += 1