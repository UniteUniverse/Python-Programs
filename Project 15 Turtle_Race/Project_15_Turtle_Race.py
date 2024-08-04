from turtle import*
from random import*
is_race_on=False
screen=Screen()
screen.setup(height=400,width=500)
user_bet=screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Choose between blue, red, orange, green, yellow, purple colours. Enter your colour: ")
print(user_bet)
colours=["red","orange","yellow","green","blue","purple"]
y_position=-100
all_turtles=[]
for turtle_index in range(0,6):
    new_turtle=Turtle()
    new_turtle.penup()
    new_turtle.shape("turtle")
    new_turtle.goto(x=-230,y=y_position)
    new_turtle.color(colours[turtle_index])
    y_position+=50
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on=True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winning_colour=turtle.pencolor()
            if winning_colour==user_bet:
                print(f"You have won the race! The {winning_colour} turtle is the winner!")
            else:
                print(f"You have lost the race! The {winning_colour} turtle is the winner!")
        rand_distance=randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()