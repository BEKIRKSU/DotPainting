import colorgram
import turtle
import random

# rgb_colors = []
# colors = colorgram.extract('hirstpntg.jpeg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
# All of the above was done so we could generate a random list which we copied from the terminal
# to the line below. And then we can copy out the code above because it's no longer needed.
# Inside the turtle module there's a Turtle class.
turtle.colormode(255)
painter = turtle.Turtle()
color_list = [(246, 242, 235), (247, 240, 244), (239, 242, 247), (237, 245, 240), (212, 149, 95), (215, 80, 62), (47, 94, 142), (231, 218, 92), (148, 66, 91), (22, 27, 40), (155, 73, 60), (122, 167, 195), (40, 22, 29), (39, 19, 15), (209, 70, 89), (192, 140, 159), (39, 131, 91), (125, 179, 141), (75, 164, 96), (229, 169, 183), (15, 31, 22), (51, 55, 102), (233, 220, 12), (159, 177, 54), (99, 44, 63), (35, 164, 196), (234, 171, 162), (105, 44, 39), (164, 209, 187), (151, 206, 220)]

# 10 by 10, dot size 20, spaced around 50 spaces.
# Look at the documentation and figure out how to move the turtle to draw these dots.
# First we import turtle and then we create and save the object, inside as 'painter'.

# because we are using the rgb colour which has the rgb values, between 0-255 we first have to
#  get the turtle module to change its color mode to 255. Check above.
# size 20 and random colour below.

# This changes the angle at which the painter moves.
painter.setheading(220)
painter.penup()
painter.forward(300)
painter.setheading(0)

for _ in range(10):
    painter.pendown()
    painter.dot(20, random.choice(color_list))
    painter.penup()
    painter.forward(50)

painter.setheading(90)
painter.forward(50)
painter.setheading(180)
# When we run it now it paints a dot and quickly flashes away. So we create a screen object
# From the turtle module, and the class is called 'Screen', and then we change the behaviour of our screen.
screen = turtle.Screen()
screen.exitonclick()
# So it only disappears on click.






