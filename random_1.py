#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
t = trtl.Turtle()
t.pensize(40)
t.circle(20)

variable1 = 6

leg_length = 70
z = 500 / variable1

t.pensize(5)
n = 0

while (n < variable1):
  t.goto(0,0)
  t.setheading(z*n)
  t.forward(leg_length)
  n = n + 1
t.hideturtle()

wn = trtl.Screen()