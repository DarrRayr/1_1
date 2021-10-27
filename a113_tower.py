import turtle as trtl

t = trtl.Turtle()
t.speed(0)
t.pensize(5)

x = -150
y = -150

num_floors = 63
floor = 0

while floor < num_floors:
	t.penup()
	t.goto(x, y)
	t.color("gray")
	y = y + 5
	floor = floor + 1
	rem = floor % 3
	if rem == 0:
		t.pencolor("blue")
	if floor == 22:
		x = x + 75
		y = y - 110
	if floor == 43:
		x = x + 75
		y = y - 105

	

	
	
	


	t.pendown()
	t.forward(50)

wn = trtl.Screen
wn.mainloop()
