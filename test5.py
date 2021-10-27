import turtle as trtl
import random
t = trtl.Turtle()
a = -400
b = -400
t.speed(5)
t.pensize(5)
for x in range(5):
	a = a + 100
	b = b + 100
	t.penup()
	t.setposition(a, b)
	t.pendown()
	
	randint2 = random.randrange(1,8)
	
	if randint2 == 1:
		t.color("red")
	elif randint2 == 2:
		t.color("blue")
	elif randint2 == 3:
		t.color("green")
	elif randint2 == 4:
		t.color("pink")
	elif randint2 == 5:
		t.color("purple")
	elif randint2 == 6:
		t.color("yellow")
	elif randint2 == 7:
		t.color("orange")
	elif randint2 == 8:
		t.color("turqoise")
	for x in range(5):
		randint1 = random.randrange(1,5)
		rsize = random.randrange(20,150)
		if randint1 == 1:
			t.begin_fill()
			t.circle(rsize)
			t.end_fill()
		elif randint1 == 2:
			t.begin_fill()
			t.circle(rsize,360,4)
			t.end_fill()
		elif randint1 == 3:
			t.begin_fill()
			t.circle(rsize,360,3)
			t.end_fill()
		elif randint1 == 4:
			t.begin_fill()
			t.circle(rsize,360,8)
			t.end_fill()
		elif randint1 == 5:
			t.begin_fill()
			t.circle(rsize,360,30)
			t.end_fill()






wn = trtl.Screen()
wn.mainloop()