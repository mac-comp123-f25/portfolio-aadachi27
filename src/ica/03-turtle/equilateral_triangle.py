# draw filled in equilateral triangle

import turtle
wind = turtle.Screen()
tina = turtle.Turtle()

wind.bgcolor("turquoise")

tina.begin_fill()

for sides in range(3):
    tina.forward(100)
    tina.left(120)

tina.end_fill()

wind.exitonclick()
