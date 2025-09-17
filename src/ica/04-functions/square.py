# function that draws a square

import turtle

def turtle_square(sqTurt, side_len):
    sqTurt = turtle.Turtle()
    for sides in range(4):
        sqTurt.forward(side_len)
        sqTurt.left(90)

win = turtle.Screen()
tt = turtle.Turtle

turtle_square(tt, 100)
turtle_square(tt, 75)
turtle_square(tt, 25)
turtle_square(tt, 5)

win.exitonclick()

