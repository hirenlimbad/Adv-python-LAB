# practical 24
# Draw color-filled shapes(square,rectangle,and circle) using Turtle

import turtle as t
t.color('red')

t.penup()
t.goto(0,-100)
t.pendown()


t.begin_fill()
for j in range(4):
	t.forward(50)
	t.left(90)
t.end_fill()

t.begin_fill()
t.penup()
t.goto(0,-10)
t.pendown()


for j in range(2):
	t.forward(50)
	t.left(90)
	t.forward(80)
	t.left(90)
t.end_fill()

t.begin_fill()
t.penup()
t.goto(0,200)
t.pendown()
t.circle(50)
t.end_fill()

t.done()