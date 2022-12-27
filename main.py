import random
from turtle import Turtle, Screen
import turtle as t

turtle = Turtle()
screen = Screen()


t.colormode(255)

turtle.shape("turtle")
turtle.speed(100)


def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def draw_stereograph(size_of_gap):

    for i in range(int(360 / size_of_gap)):
        turtle.color(random_colors())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + size_of_gap)


draw_stereograph(5)


screen.exitonclick()
