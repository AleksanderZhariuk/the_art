from turtle import Turtle, Screen
from random import choice


def return_to_position(step_up):
    x_position = -450
    y_position = -350 + step_up
    return x_position, y_position


def dot_drawing():
    for dot in range(10):
        arrow.pendown()
        random_color = choice(color_list)
        arrow.dot(35, random_color)
        arrow.penup()
        arrow.forward(100)


color_list = [
            (214, 153, 73), (174, 47, 78), (244, 233, 237), (139, 30, 54), (36, 43, 72), (237, 217, 95),
            (160, 182, 26), (34, 108, 151), (212, 67, 99), (109, 187, 203), (22, 144, 80), (41, 49, 113),
            (238, 72, 55), (72, 185, 108), (142, 86, 61), (199, 123, 166), (76, 26, 47), (60, 41, 39),
            (237, 200, 1), (236, 165, 192), (4, 187, 195), (28, 49, 46), (78, 127, 192), (91, 187, 145),
            (1, 87, 119), (162, 216, 184), (77, 70, 43)
            ]


arrow = Turtle()
screen = Screen()

#   FOR WORKING RGB COLOURS
screen.colormode(255)

#   CURSOR FEATURES
arrow.shape('classic')
arrow.speed(7)
arrow.fillcolor('gray')
arrow.penup()

#   START POSITION
arrow.setposition(-450, -350)

step = 0
for _ in range(10):
    step += 80
    dot_drawing()
    x_pos, y_pos = return_to_position(step)
    arrow.setposition(x_pos, y_pos)

screen.exitonclick()
