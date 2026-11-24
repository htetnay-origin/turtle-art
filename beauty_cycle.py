from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.setup(width=800, height=600)
screen.screensize(800, 600)
screen.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

tim.speed("fastest")

for i in range(100):
    tim.color(random_color())
    tim.circle(100)
    current_heading = tim.heading()
    tim.setheading(current_heading+10)

screen.exitonclick()