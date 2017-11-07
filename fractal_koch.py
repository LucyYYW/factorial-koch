from drawingpanel import *
import math
panel = DrawingPanel(1000,1000)
canvas = panel.canvas
sqrt3 = math.sqrt(3)


def koch(x,y,side,n):
	if n <= 0:
		return None
	canvas.create_polygon(x-side*sqrt3/6, y-side/2, x+side*sqrt3/3, y, x-side*sqrt3/6, y+side/2, outline="red",fill="white")
	canvas.create_polygon(x-side*sqrt3/3, y, x+side*sqrt3/6, y-side/2, x+side*sqrt3/6, y+side/2, outline="red",fill="white")
	koch(x-side*sqrt3/9,y-side/3, side/3,n-1)
	koch(x+side*sqrt3/9,y-side/3, side/3,n-1)
	koch(x-side*sqrt3/9*2,y, side/3,n-1)
	koch(x+side*sqrt3/9*2,y, side/3,n-1)
	koch(x-side*sqrt3/9,y+side/3, side/3,n-1)
	koch(x+side*sqrt3/9,y+side/3, side/3,n-1)
	canvas.create_polygon(x,y-side/3, x+side*sqrt3/6,y-side/6, x+side*sqrt3/6,y+side/6, x,y+side/3, x-side*sqrt3/6,y+side/6, x-side*sqrt3/6,y-side/6,fill="white",outline="white",width=1)

def main():
	n = int(input("input an integer"))
	panel.set_background("white")
	side = 800
	x = 500
	y = 500	
	koch(x,y,side,n)


main()