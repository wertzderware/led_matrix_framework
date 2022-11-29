import matrix
from rpi_ws281x import Color

matrix = matrix.Matrix(13, 23, 100)
# matrix.test_colors()


heart = [
    '00110001100',
    '01001010010',
    '10000100001',
    '10000000001',
    '01000000010',
    '00100000100',
    '00010001000',
    '00001010000',
    '00000100000'
]

heart_2 = [
    '00110001100',
    '01111011110',
    '11111111111',
    '11111111111',
    '01111111110',
    '00111111100',
    '00011111000',
    '00001110000',
    '00000100000'
]

# matrix.test()
# matrix.test_colors()

# matrix.draw_shape(heart_2, (1, 10), Color(255, 0, 0), True)
# matrix.draw_shape(heart, (1, 10), Color(255, 255, 255))
# matrix.pixels.show()

# matrix.scroll_shape([heart, heart_2, heart], [Color(255, 0, 0), Color(255, 255, 255), Color(255, 255, 0)])
# matrix.scroll_shape([heart_2], [Color(0, 0, 255)])
matrix.clear(True) 

input()
