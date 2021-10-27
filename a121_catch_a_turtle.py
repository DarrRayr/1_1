# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
sq = trtl

#-----game configuration----
sqshape = "square"
sqsize = 1
sqcolor = "purple"
sqpensize = 3
score = 0


#-----initialize turtle-----
trtl.Turtle()
sq.shape(sqshape)
sq.shapesize(sqsize)
sq.fillcolor(sqcolor)
sq.pensize(sqpensize)


#-----game functions--------
def sq_clicked(x,y):
	update_score()
	change_position()

def draw_coord_plane():
	sq.penup()
	sq.setposition(-200,-150)
	sq.pendown()
	sq.left(90)
	for x in range(2):
		sq.forward(300)
		sq.right(90)
		sq.forward(400)
		sq.right(90)

def change_position():
	x = rand.randint(-200,200)
	y = rand.randint(-150,150)
	sq.penup()
	sq.setposition(x,y)
	sq.pendown()
	
def update_score():
	score =+ 1
	print(score)



#-----events----------------
sq.onclick(sq_clicked)

draw_coord_plane()


wn = trtl.Screen()
wn.mainloop()

wn.onclick(sq_clicked)