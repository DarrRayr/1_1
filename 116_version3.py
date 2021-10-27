#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
t = trtl.Turtle()

# Create a spider body
t.pensize(40)
t.circle(20)

#configure spider legs
number_of_legs = 8

leg_length = 70
leg_spacing = 300 / number_of_legs

t.pensize(5)
req = 0

#draw legs
while (req<number_of_legs):
	t.goto(0,20)
	t.setheading(leg_spacing*req)
	if req == 4:
		t.setheading(leg_length*req-30)
	t.forward(leg_length)
	req = req +1

eye_color = ("white")
eye_size = 1
t.shape("circle")
t.color(eye_color)
t.penup()
t.goto(0,0)
t.pendown()
t.circle(eye_size)
t.penup()
t.goto(20,20)
t.pendown()
t.circle(eye_size)

t.hideturtle()



wn = trtl.Screen()
wn.mainloop()