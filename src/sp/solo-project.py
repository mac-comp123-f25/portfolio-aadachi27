

import turtle
turt = turtle.Turtle()
win = turtle.Screen()
turt.speed(0)

import random

def draw_star(size, color):
    turt.pencolor(color)
    turt.fillcolor(color)
    turt.left(72)
    turt.begin_fill()
    for x in range(5):
        turt.forward(size)
        turt.left(72)
        turt.forward(size)
        turt.right(144)
    turt.end_fill()

def draw_star_circle(rad, num, color):
    turt.penup()
    turt.right(90)
    turt.forward(rad)
    turt.left(90)
    for x in range(num):
        turt.circle(rad, 360 / num)
        turt.right(72)
        turt.pendown()
        draw_star(rad / 10, color)
        turt.penup()

def rand_star_circle(num, color1, color2, color3):
    for color in [color1, color2, color3]:
        draw_star_circle(random.randrange(10, 300), random.randrange(5, 20), color)
        turt.penup()
        turt.goto(0,0)
        turt.pendown()

#draw_star(100, "purple")
#draw_star_circle(100, 8, "purple")
color1 = input('Pick a color: ')
color2 = input('Pick another color: ')
color3 = input('Pick another color: ')
rand_star_circle(3, color1, color2, color3)


win.exitonclick()