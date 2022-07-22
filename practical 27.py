# Draw an indian flag and an olympic symbol using Turtle
def flag():
	import turtle as t

	t.speed(5)
	def box(x,y):
		t.penup()
		t.goto(x,y)
		t.pendown()
		t.forward(700)
		t.right(90)
		t.forward(110)
		t.right(90)
		t.forward(700)
		t.right(90)
		t.forward(110)
		t.right(90)

	x = -350
	y = 160

	color = ['orange','white','green']
	for i in color:
		t.color(i)
		t.begin_fill()
		box(x,y)
		t.end_fill()
		y = y - 110

	t.penup()
	t.goto(0,-60)
	t.pendown()
	t.color('blue')
	t.pensize(4)
	t.circle(55)
	t.pensize(3)

	t.penup()
	t.goto(0,0)
	t.pendown()
	for j in range(24):
		t.goto(0,0)
		t.left(15)
		t.forward(53)

	t.hideturtle()
	t.done()

def olympics():

	import turtle as t
	t.speed(5)
	t.pensize(5)

	x = -200
	y = 0

	l1 = [-110,0,110]
	l2 = [55,-55]

	co1 = ['Blue','black','red']
	co2 = ['green','yellow']
	try:
		for j in l1:
			t.penup()
			t.goto(j,y)
			t.pendown()
			t.color(co1[0])
			t.circle(70)
			co1.remove(co1[0])

	except:
		pass

	try:
		y = -110
		for j in l2:
			t.penup()
			t.goto(j,y)
			t.pendown()
			t.color(co2[0])
			t.circle(70)
			co2.remove(co2[0])
	except:
		pass
	t.done()


n = int(input('For indian flag Enter 1 and for olympic logo type 2 and hit ENTER: '))
if n == 1:
	flag()
elif n == 2:
	olympics()
