from turtle import Turtle, Screen
import turtle
tim=Turtle()
tim.shape("turtle")
screen=Screen()
tim.pensize(5)

def move_forwards():
    tim.forward(20)
screen.onkeypress(key="w", fun=move_forwards)

def move_backwards():
    tim.backward(20)
screen.onkeypress(key="s", fun=move_backwards)

def clockwise():
    new_heading=tim.heading() +10
    tim.setheading(new_heading)
screen.onkeypress(key="a", fun=clockwise)

def counter_clockwise():
    new_heading= tim.heading() -10
    tim.setheading(new_heading)
screen.onkeypress(key="d",fun=counter_clockwise)


def reset():
    tim.reset()
    tim.pensize(5)
screen.onkey(key="c", fun=reset)


screen.listen()
screen.exitonclick()

