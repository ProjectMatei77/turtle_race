import turtle
from turtle import *
import random

is_race_on= False
screen=Screen()
screen.setup(500,400)
user_bet= screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors=["red","orange","yellow","green","blue","purple"]
y_positions=[-60,-30, 0, 30, 60, 90]
all_turtles=[]
def create_turtle():
    for x in range(0,6):
        new_turtle=Turtle("turtle")
        new_turtle.penup()
        new_turtle.color(colors[x])
        new_turtle.goto(x=-230, y=y_positions[x])
        all_turtles.append(new_turtle)
create_turtle()

number=[0, 2,4,6,9,12,15,20]

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on= False
            winning_color= turtle.pencolor()
            if winning_color==user_bet:
                print(f"Congrats, you WON! {user_bet}")
            else:
                print(f"You lost, winner turtle was: {winning_color}")
            # print(turtle.color())
        random_distance=random.choice(number)
        turtle.forward(random_distance)

screen.exitonclick()
