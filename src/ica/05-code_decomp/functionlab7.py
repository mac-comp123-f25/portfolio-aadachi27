'''draw four flowers in a cross formation using layers of green, pink,
and purple circles with a turtle stamp in the middle, with four turtles -
one drawing each color circle and one that makes the middle stamp '''

import turtle
import math

def drawAll():
    '''draw four flowers in a cross formation using layers of green, pink,
    and purple circles with a turtle stamp in the middle, with four turtles -
    one drawing each color circle and one that makes the middle stamp '''
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

    drawFlower(sepalTurtle, petalTurtle, centerTurtle, stampTurtle, 0, 0)

    drawFlower(sepalTurtle, petalTurtle, centerTurtle, stampTurtle, 0, 220)

    drawFlower(sepalTurtle, petalTurtle, centerTurtle, stampTurtle, 220, 0)

    drawFlower(sepalTurtle, petalTurtle, centerTurtle, stampTurtle, 0, -220)

    drawFlower(sepalTurtle, petalTurtle, centerTurtle, stampTurtle, -220, 0)

    win.exitonclick()

def drawFlower(turt1, turt2, turt3, turt4, centerX, centerY):
    '''draw five flowers each at different center inputs with four different turtles'''
    drawFiveCircles(turt1, 50, centerX, centerY)
    drawFiveCircles(turt2, 25, centerX, centerY)
    drawCenterCircle(turt3, centerX, centerY - 15)
    drawBee(turt4, centerX - 2, centerY)

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

def drawBee(turt, centerX, centerY):
    '''stamp turtle in the middle of center circle of flower
    input name of turtle and x- and y-coordinates of center
    circle'''
    turt.up()
    turt.goto(centerX, centerY)
    turt.down()
    turt.stamp()

drawAll()