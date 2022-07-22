import turtle
from turtle import *

class Paddle:
    def __init__(self,start_pos):
        self.start_pos=start_pos

        self.p=Turtle()
        self.p.penup()
        self.p.shape("square")
        self.p.color("white")
        self.p.turtlesize(stretch_wid=5,stretch_len=1)
        self.p.setpos(self.start_pos)

    def move_up(self):
        self.p.penup()
        self.p.goto(self.p.xcor(),self.p.ycor()+20)

    def move_down(self):
        self.p.penup()
        self.p.goto(self.p.xcor(),self.p.ycor()-20)

    def reset(self):
        self.p.setpos(self.start_pos)
