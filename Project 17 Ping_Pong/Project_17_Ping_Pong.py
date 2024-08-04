from turtle import *
from paddle import*
from ball import*
from scoreboard_ping import*
import time

screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Ping-Pong")
screen.tracer(0)

r_paddle=Paddle(x_coordinate=350,y_coordinate=0)
l_paddle=Paddle(x_coordinate=-350,y_coordinate=0)
ball=Ball()
scoreboard=Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
time_sleep=0.1
game_is_on=True
while game_is_on:
    time.sleep(time_sleep)
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
       
    if ball.distance(r_paddle.paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle.paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()
        time_sleep/=1.4
    if ball.xcor()>380 :
        ball.reset_position() 
        scoreboard.l_point()
        time_sleep=0.1
    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()
        time_sleep=0.1
screen.exitonclick()