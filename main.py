from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("arrow")
start = 3
angle = 360
count = 8


screen = Screen()
screen.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

tim.color(random_color())




screen.setup(width=800, height=600)
screen.screensize(800, 600)

while count > 0 :
    tim.color(random_color())
    for i in range(start):
        tim.forward(100)
        tim.left(angle/start)
    start += 1
    count -= 1






screen.exitonclick()