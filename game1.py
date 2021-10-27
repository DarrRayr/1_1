import time
import math
print("Welcome to battle sim")
print("")
time.sleep(2)
bag = [""]
health = 100
def wolf_battle():
	print("You have ran into a wolf!")
	wolf_health = 100
	descision = 1
	if descision == 1:
		print("Bag | Battle | Run")
		descision1 = input(" ")
		if descision1.lower == ("bag"):
		
			print(bag)
			if len(bag) == 0:
				print("There is nothing in your bag!")
				descision = 1

	