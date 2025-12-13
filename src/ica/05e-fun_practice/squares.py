# draw 8 nested squares, the smallest with side length 10, increasing side length by 10

import turtle

def draw_nested_squares(turt):
    for x in range(9):
        for sides in range(4):
            turt.forward(10 * x)
            turt.left(90)

win = turtle.Screen()
tt = turtle.Turtle()
draw_nested_squares(tt)
win.exitonclick()
