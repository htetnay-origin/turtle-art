# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
#
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle
import turtle as turtle_module
import random
screen = turtle_module.Screen()
screen.setup(width=800, height=600)
screen.screensize(800, 600)
tim = turtle_module.Turtle()
turtle.colormode(255)
tim.penup()
tim.hideturtle()

color_list = [(216, 209, 199), (185, 82, 28), (203, 158, 107), (53, 105, 137), (199, 162, 26), (148, 70, 102), (212, 198, 133), (116, 157, 174), (129, 173, 160), (61, 117, 81), (158, 135, 158), (27, 46, 69), (193, 95, 86), (30, 59, 115), (81, 143, 161), (45, 33, 48), (26, 77, 85), (182, 95, 106), (36, 47, 34), (73, 92, 24), (204, 210, 205), (95, 146, 105), (35, 86, 73), (40, 39, 31), (207, 211, 215), (72, 49, 85), (218, 210, 212), (218, 181, 170), (177, 200, 184), (142, 40, 20)]

tim.setheading(225)
tim.forward(250)
tim.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen.exitonclick()