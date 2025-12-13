# user input controls turtle

import turtle

def tele_turtle(n):
  win = turtle.Screen()
  tele_t = turtle.Turtle()
  for i in range(n):
    move = input("Enter next move: ")
    do_move(tele_t, move)
  win.exitonclick()

def do_move(turt, move):
    if move == 'f':
        turt.forward(15)
    elif move == 'b':
        turt.backward(15)
    elif move == 'r':
        turt.right(90)
    elif move == 'l':
        turt.left(90)
    else:
        return "Warning: invalid input"

tele_turtle(10)