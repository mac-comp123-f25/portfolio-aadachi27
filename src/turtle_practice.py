# function that draws a pink and purple flower of inputted center diameter
# and number of petals

def draw_flower(diam, petals):
    import turtle
    import random

    window = turtle.Screen()
    flower = turtle.Turtle()

    flower.speed(0)
    flower.color("purple")
    flower.fillcolor("violet")

    for times in range(petals):
        flower.begin_fill()
        flower.circle((2 * diam), 90)
        flower.left(90)
        flower.circle((2 * diam), 90)
        flower.end_fill()
        flower.left(90)
        flower.right(360 / petals)

    # draw center dot
    flower.color("purple")
    flower.dot(1.2 * diam)
    flower.dot(diam)
    # draw a random sprinkling of dots inside of center
    flower.color("black")
    flower.up()
    print(type(diam))
    for times in range(diam):
        x = random.randint(0, (diam // 2))
        a = random.randint(0, 360)
        flower.right(a)
        flower.forward(x)
        flower.dot(diam // 12)
        flower.back(x)

    window.exitonclick()

draw_flower(100, 20)