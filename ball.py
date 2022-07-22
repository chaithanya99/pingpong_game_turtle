from turtle import *
class Ball:
    def __init__(self):
        self.b=Turtle()
        self.b.color("white")
        self.b.penup()
        self.b.shape("circle")
        self.x=10
        self.y=10
    def move(self):
        self.b.goto(self.b.xcor()+self.x,self.b.ycor()+self.y)
    def bounce(self):
        self.y=-self.y
    def bounce_paddle(self):
        self.x*=-1
    def reset(self):
        self.b.goto(0,0)
        self.x*=-1
        self.y=10