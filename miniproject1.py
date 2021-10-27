import turtle as trtl
import time
 
t = trtl.Turtle()


def make_shape(name):

	print("Hello,"+name, "welcome to the art center!")
	print(" ")
	time.sleep(2)
	print("Here you will make a piece of art you like!")
	print(" ")
	time.sleep(2)
	print("First start with a color!")
	print(" ")
	time.sleep(2)
	color = input("Insert a color: ")
	print(" ")
	time.sleep(2)
	print("Now for a shape!")
	print(" ")
	time.sleep(2)
	shape = input("Insert a shape: ")
	print(" ")
	time.sleep(2)
	print("Now for the size!")
	print(" ")
	time.sleep(2)
	size = int(input("Insert a number: "))




	t.color(color)
	t.shape(shape)
	t.pensize(size)

	t.stamp()



customers = ["Josh", "Drake", "Jerry", "Tom"]
for name in range(len(customers)):
	
	make_shape(name)
	order = order+1





wn = trtl.Screen()
wn.mainloop()


