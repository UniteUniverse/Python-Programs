from turtle import*
class Paddle:
    def __init__(self,x_coordinate,y_coordinate):
        self.paddle=Turtle()
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_len=1,stretch_wid=5)
        self.paddle.penup()
        self.paddle.goto(x=x_coordinate,y=y_coordinate)
        self.go_up()
        self.go_down
    def go_up(self):
        new_y=self.paddle.ycor()+20
        self.paddle.goto(self.paddle.xcor(),new_y)

    def go_down(self):
        new_y=self.paddle.ycor()-20
        self.paddle.goto(self.paddle.xcor(),new_y)
    