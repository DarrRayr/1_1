#   a116_ladybug.py
import turtle as trtl
ladybug = trtl.Turtle()

number_of_legs = 6

leg_length = 60
leg_spacing = 240 / number_of_legs

ladybug.pensize(5)
req = 0

#draw legs
while (req<number_of_legs):
	ladybug.goto(0,-30)
	ladybug.setheading(leg_spacing*req)
	if req == 3:
		ladybug.setheading(leg_spacing*req+90)
	ladybug.forward(leg_length)
	

	
	

	req = req +1

ladybug.penup()
ladybug.goto(0,0)
ladybug.pendown()
ladybug.setheading(0)

# create ladybug head

ladybug.pensize(40)
ladybug.circle(5)

# and body
ladybug.penup()
ladybug.goto(0, -55) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
num_dots = 1
xpos = -20
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
while (num_dots <= 2 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 20)
  ladybug.pendown()
  ladybug.circle(2)
# position next dots
  ypos = ypos + 25
  xpos = xpos + 5
  num_dots = num_dots + 1



ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()