# turtle draws three spokes coming out from center

import turtle
wind = turtle.Screen()
curtis = turtle.Turtle()

for times in range(3):
    curtis.forward(100)
    curtis.backward(100)
    curtis.left(120)

wind.exitonclick()