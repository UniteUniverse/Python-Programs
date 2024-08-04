from turtle import *
class Snake:
    def __init__(self):
        self.x_coordinate=0
        self.segment=[]
        self.new_turtle()
        self.head=self.segment[0]

    def new_turtle(self):
        for turtle_index in range(0,3):
             self.add_segment(position)

    def add_segment(self,position):
        pratyush=Turtle(shape="square")
        pratyush.penup()
        pratyush.goto(x=self.x_coordinate,y=0)
        pratyush.color("white")
        self.x_coordinate-=20
        self.segment.append(pratyush)

    def extend(self):
        self.add_segment(self.segment[-1].position())
    
    def move(self):
        for seg_num in range(len(self.segment)-1,0,-1):
            new_x=self.segment[seg_num-1].xcor()
            new_y=self.segment[seg_num-1].ycor()
            self.segment[seg_num].goto(new_x,new_y)
        self.segment[0].forward(20)

    def upward(self):
        if self.segment[0].heading()!=270:
            self.segment[0].setheading(90)
    def downward(self):
        if self.segment[0].heading()!=90:
            self.segment[0].setheading(270)
    def leftward(self):
        if self.segment[0].heading()!=0:
            self.segment[0].setheading(180)
    def rightward(self):
        if self.segment[0].heading()!=180:
            self.segment[0].setheading(0)
    
    def reset(self):
        for seg in self.segment:
            seg.goto(1000,1000)
        self.segment.clear()
        self.new_turtle()
        self.head=self.segment[0]