from turtle import *
class Score:
    def __init__(self,pos):
        self.pos=pos
        self.soc=Turtle()
        self.soc.color("white")
        self.score=0
        self.soc.penup()
        self.soc.goto(self.pos)
        self.soc.hideturtle()
        self.display()

    def display(self):
        self.soc.clear()
        self.soc.write(str(self.score),font=('Arial',20,'normal'))
        self.score+=1

    def win(self,str):

        self.soc.goto(-50,0)
        self.soc.write(str+" player won", font=('Arial', 20, 'normal'))
