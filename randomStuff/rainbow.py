from matrix import Matrix
from rpi_ws281x import Color
from time import sleep

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

colors = [ 
    Color(255, 0, 0), # red
    Color(255, 10, 0), 
    Color(255, 25, 0), 
    Color(255, 165, 0), 
    Color(255, 195, 0),
    Color(255, 225, 0),
    Color(255, 255, 0),
    Color(170, 213, 0),
    Color(50, 200, 0),
    Color(0, 170, 0), # green
    Color(0, 85, 85),
    Color(0, 43, 170),
    Color(0, 0, 255), # blue
    Color(25, 0, 213),
    Color(50, 0, 172),
    Color(75, 0, 130),
    Color(129, 43, 166),
    Color(184, 87, 202),
    Color(255, 20, 20)
]

matrix = Matrix(13, 23, 255)

def test_colors(matrix):
    matrix.draw_rectangle((0, 0), (matrix.width - 1, matrix.height - 1), Color(255, 255, 255))
    matrix.draw_rectangle((1, 1), (matrix.width - 2, matrix.height - 2), Color(255, 255, 255))
    shift = 0
    while True:
        for i in range(len(colors)):
            y = (i + shift) % len(colors) + 2
            matrix.draw_line((2, y), (matrix.width - 3, y), colors[i % len(colors)])
        matrix.pixels.show()
        shift += 1
        sleep(0.07)

test_colors(matrix)