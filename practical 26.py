# practical 26.py
# Draw smiling face emoji and rainbow using turtle.

# import turtle as t


def smile():
	import turtle as t
	t.color('#9400D3')
	t.begin_fill()
	t.pensize(4)
	t.speed(3)
	t.penup()
	t.goto(0,-100)
	t.pendown()
	t.circle(200)
	t.end_fill()

	t.color('white')
	t.penup()
	t.goto(-90,40)
	t.left(270)
	t.pendown()
	t.circle(100,180)

	t.color('white')
	t.begin_fill()
	t.penup()
	t.goto(-90,180)
	t.pendown()
	t.circle(15)
	t.end_fill()

	# t.color('black')
	t.penup()
	t.goto(100,190)
	t.pendown()
	t.begin_fill()
	t.circle(15)
	t.end_fill()

	t.color('white')
	t.penup()
	t.goto(-30,50)
	t.right(90)
	t.pendown()
	t.fd(70)
	t.bk(35)

	t.left(90)
	t.fd(30)
	t.shape('triangle')
	t.done()

def rainbow():
	import turtle as t
	color = ['#9400D3','#4B0082','#0000FF','#00FF00','#FFFF00','#FF7F00','#FF0000']
	t.pensize(20)
	r = 40
	x = 0
	t.left(90)
	for j in color:
		t.penup()
		t.goto(x,0)
		t.pendown()
		t.color(j)
		t.circle(r,180)
		t.left(180)
		r = r + 20
		x = x + 20
	t.done()

w = int(input('Enter a 1 for smile or enter 2 for rainbow...'))
if w == 1:
	smile()
if w == 2:
	rainbow()