from turtle import *
from snake import *
from food import *
from scoreboard import*
import time
screen=Screen()
screen.setup(height=600,width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake=Snake()

food=Food()
score=Score()

screen.listen()
screen.onkey(fun=snake.upward,key="Up")
screen.onkey(fun=snake.downward,key="Down")
screen.onkey(fun=snake.leftward,key="Left")
screen.onkey(fun=snake.rightward,key="Right")

game_is_on=True
while game_is_on: 
    screen.update()
    time.sleep(0.1)  
    snake.move()

    if snake.head.distance(food)<15:
        food.refresh()
        score.increase_score()
        snake.extend()

    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        score.reset_score()
        snake.reset()

    for seg in snake.segment[1:]:
        if snake.head.distance(seg)<10:
            score.reset_score()
            snake.reset()
        

screen.exitonclick()