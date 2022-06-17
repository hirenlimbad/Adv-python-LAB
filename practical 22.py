# Draw square,recrange,and circle using Turtle.


import turtle as t 

t.color("white")
t.goto(-200,110)
t.color("black")
t.pensize(3)


for j in range(4):
	t.forward(65)
	t.right(90)


t.forward(68)
t.color("white")
t.goto(90,40)
t.color("black")
t.circle(100)


t.color("white")
t.goto(-90,-90)
t.color("black")

for j in range(2):
	t.right(90)
	t.forward(180)
	t.right(90)
	t.forward(65)
t.done()
