#a114_nested_loops_2
import turtle as trtl

t = trtl.Turtle()
t.shape("circle")
t.hideturtle()
t.penup()

y = -200
while (y < 200):
	y = y + 50
	x = -200
	t.goto(x,y)
	t.color("purple")
	t.stamp()
	while (x < 100):
		x = x +50
		t.goto(x,y)
		t.color("orange")
		t.stamp()

wn = trtl.Screen()
wn.mainloop()

