# draw a chess-board using turtle module
import turtle as t
t.shapesize(3)
t.shape('square')

def box():
	for j in range(4):
		t.color('black')
		t.stamp()
		t.color('white')
		t.penup()
		t.forward(120)
		t.pendown()
		t.stamp()

def box1():
	for i in range(4):
		t.penup()
		t.forward(120)
		t.pendown()
		t.color('black')
		t.stamp()


x = -600
y = 300

t.penup()
t.goto(x,y)
t.pendown()

for j in range(4):
	box()
	y = y-60
	x = x-60
	t.penup()
	t.goto(x,y)
	t.pendown()
	box1()
	y = y - 60
	x = x + 60
	t.penup()
	t.goto(x,y)
	t.pendown()

# x = -650
# y = 330
# t.penup()
# t.goto(x,y)
# t.pendown()

# t.forward(500)
# t.right(90)
# t.forward(480)
# t.right(90)
# t.forward(480)
# t.right(90)
# t.forward(470)

t.hideturtle()
t.done()
