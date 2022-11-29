from matrix import Matrix
from rpi_ws281x  import Color
from time import sleep

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

matrix = Matrix(13, 23, 50)
matrix.clear(True)
count = 0
#Rahmen
def frameBuild():
	matrix.draw_rectangle((0,0),(12,22), Color(255,255,255))
	matrix.draw_rectangle((1,1),(11,21), Color(255,255,255))
#	matrix.pixels.show()
#	sleep(0.3)
#	matrix.draw_rectangle((0,0),(12,22), Color(0,0,0))
#	matrix.draw_rectangle((1,1),(11,21), Color(0,0,0))
#	matrix.pixels.show()
#	sleep(0.4)
#	frameBuild()

def FlagDraw(shift):	
	matrix.draw_line((2,(shift+2)%19+2),(10,(shift+2)%19+2),Color(255,255,0))
	matrix.draw_line((2,(shift+3)%19+2),(10,(shift+3)%19+2),Color(255,255,0))
	matrix.draw_line((2,(shift+4)%19+2),(10,(shift+4)%19+2),Color(255,255,0))
	matrix.draw_line((2,(shift+5)%19+2),(10,(shift+5)%19+2),Color(255,255,0))
	matrix.draw_line((2,(shift+6)%19+2),(10,(shift+6)%19+2),Color(255,255,0))
	matrix.draw_line((2,(shift+7)%19+2),(10,(shift+7)%19+2),Color(255,255,0))

	matrix.draw_line((2,(shift+8)%19+2),(10,(shift+8)%19+2),Color(255,0,0))
	matrix.draw_line((2,(shift+9)%19+2),(10,(shift+9)%19+2),Color(255,0,0))
	matrix.draw_line((2,(shift+10)%19+2),(10,(shift+10)%19+2),Color(255,0,0))
	matrix.draw_line((2,(shift+11)%19+2),(10,(shift+11)%19+2),Color(255,0,0))
	matrix.draw_line((2,(shift+12)%19+2),(10,(shift+12)%19+2),Color(255,0,0))
	matrix.draw_line((2,(shift+13)%19+2),(10,(shift+13)%19+2),Color(255,0,0))

	matrix.draw_line((2,(shift+20)%19+2),(10,(shift+20)%19+2),Color(255,255,255))

while True:
	count = count + 1
	if count % 10 > 5:
		frameBuild()
	FlagDraw(count)
	matrix.pixels.show()	
	sleep(0.1)
	matrix.clear()
