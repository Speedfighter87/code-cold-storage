import random
import turtle

t = turtle.Turtle()

while True:
	t.right(random.choice(range(0, 270, 90)))
	t.forward(100)
