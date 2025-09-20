# draw polygon with n sides

import turtle
wind = turtle.Screen()
pete = turtle.Turtle()

wind.bgcolor("turquoise")

n = 5

pete.begin_fill()

for sides in range(n):
    pete.forward(100)
    pete.left(360/n)

pete.end_fill()

wind.exitonclick()