from snake import Snake
from canvas import Canvas


canvas = Canvas()
snake = Snake()
canvas.ad_object(snake)
running = True

canvas.ad_object(snake)

def start():
    while running:
        canvas.update()

start()