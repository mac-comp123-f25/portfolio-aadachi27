'''draw four flowers in a cross formation using layers of green, pink,
and purple circles with a turtle stamp in the middle, with four turtles -
one drawing each color circle and one that makes the middle stamp '''

import turtle
import math

def drawFiveCircles(turt, radius, centerX, centerY):
    '''function drawing five equally sized circles in a circle
    inputs are turtle name, radius value, x-coordinate of center position,
    and y-coordinate of center position'''
    turt.up()
    turt.goto(centerX , centerY)
    turt.down()
    for num in range(5):
        turt.begin_fill()
        turt.circle(radius)
        turt.end_fill()
        turt.left(72)

def drawCenterCircle(turt, centerX, centerY):
    '''function drawing purple center circle
    inputs are name of turtle, and x- and y-
    coordinates of center'''
    turt.up()
    turt.goto(centerX, centerY)
    turt.down()
    turt.begin_fill()
    turt.circle(15)
    turt.end_fill()

win = turtle.Screen()
win.bgcolor("light sky blue")

sepalTurtle = turtle.Turtle()
sepalTurtle.speed(0)
sepalTurtle.color("dark green", "spring green")
sepalTurtle.hideturtle()

petalTurtle = turtle.Turtle()
petalTurtle.speed(0)
petalTurtle.color('dark red', 'light coral')
petalTurtle.hideturtle()

centerTurtle = turtle.Turtle()
centerTurtle.speed(0)
centerTurtle.color('purple4')
centerTurtle.hideturtle()

stampTurtle = turtle.Turtle()
stampTurtle.color("gold")
stampTurtle.speed(0)
stampTurtle.shape("turtle")
stampTurtle.hideturtle()

drawFiveCircles(sepalTurtle, 50, 0, 0)

drawFiveCircles(petalTurtle, 25, 0, 0)

drawCenterCircle(centerTurtle, 0, -15)

stampTurtle.up()
stampTurtle.goto(-2,0)
stampTurtle.down()
stampTurtle.stamp()

drawFiveCircles(sepalTurtle, 50, 0, 220)

drawFiveCircles(petalTurtle, 25, 0, 220)

drawCenterCircle(centerTurtle, 0, 205)

stampTurtle.up()
stampTurtle.goto(-2,220)
stampTurtle.down()
stampTurtle.stamp()

drawFiveCircles(sepalTurtle, 50, 220, 0)

drawFiveCircles(petalTurtle, 25, 220, 0)

drawCenterCircle(centerTurtle, 220, -15)

stampTurtle.up()
stampTurtle.goto(218,0)
stampTurtle.down()
stampTurtle.stamp()

drawFiveCircles(sepalTurtle, 50, 0, -220)

drawFiveCircles(petalTurtle, 25, 0, -220)

drawCenterCircle(centerTurtle, 0, -235)

stampTurtle.up()
stampTurtle.goto(-2,-220)
stampTurtle.down()
stampTurtle.stamp()

drawFiveCircles(sepalTurtle, 50, -220, 0)

drawFiveCircles(petalTurtle, 25, -220, 0)

drawCenterCircle(centerTurtle, -220, -15)

stampTurtle.up()
stampTurtle.goto(-222,0)
stampTurtle.down()
stampTurtle.stamp()

win.exitonclick()