#group members: Toma, Jaxson, Omar, Darryl
import turtle as trtl
t = trtl.Turtle()

def equation():
	t.color("black")
	t.pendown()
	equation = input("what should the equation be, in y = mx + b format please: ")
	t.setheading(0)
	splitequation = list(str(equation))
	t.speed(1)
	slope = float(splitequation[2])
	y_intercept = float(splitequation[5])
	t.penup()
	t.setposition(0,y_intercept*10)
	t.pendown()
	t.left(slope*15)
	t.forward(450)
	t.left(90)
	t.backward(10)
	t.forward(10)
	t.right(180)
	t.backward(10)
	t.forward(10)
	t.left(90)
	
	t.backward(900)
	t.left(90)
	t.forward(10)
	t.backward(10)
	t.right(180)
	t.forward(10)
	t.backward(10)
	t.left(90)
	

t.speed(0)
t.penup()
t.setposition(-390,400)
for i in range(40):
	t.right(90)
	t.pendown()
	t.forward(800)
	t.left(90)
	t.penup()
	t.forward(10)
	t.pendown()
	t.left(90)
	t.forward(800)
	t.right(90)
	t.penup()
	t.forward(10)

t.penup()
t.setposition(400,-390)
t.pendown()
t.right(270)
for i in range(40):
  t.left(90)
  t.pendown()
  t.forward(800)
  t.right(90)
  t.penup()
  t.forward(10)
  t.pendown()
  t.right(90)
  t.forward(800)
  t.left(90)  
  t.penup()
  t.forward(10)

t.penup()
t.setposition(0,0)
t.pendown()
t.pensize(2)
t.forward(400)
t.backward(800)
t.forward(400)
t.left(90)
t.forward(400)
t.backward(800)

equation()

wn = trtl.Screen()
wn.mainloop()


