import turtle
from turtle import *
from paddle import *
from ball import *
from score import *
from random import *
import time
screen=Screen()
turtle.tracer(0)
screen.bgcolor("black")
screen.title("PongGame")
screen.setup(height=600,width=800)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
game_on=True

r_score=Score((200,0))
l_score=Score((-200,0))

screen.listen()
screen.onkey(fun=r_paddle.move_up,key="Up")
screen.onkey(fun=r_paddle.move_down,key="Down")
screen.onkey(fun=l_paddle.move_up,key="w")
screen.onkey(fun=l_paddle.move_down,key="s")
ball.b.speed("slow")
while game_on:
    turtle.update()
    time.sleep(0.1)
    ball.move()
    if(ball.b.ycor()>=290 or ball.b.ycor()<=-290):
        print("ball hit wall")
        ball.bounce()
    if ball.b.xcor()>=330 and r_paddle.p.distance(ball.b)<=50:
        print("ball hit paddle")
        ball.bounce_paddle()
    if ball.b.xcor()<=-330 and l_paddle.p.distance(ball.b)<=50:
        ball.bounce_paddle()
    if ball.b.xcor()>=390 or ball.b.xcor()<=-390:
        if ball.b.xcor()>=390:
            l_score.display()
        else:
            r_score.display()
        ball.reset()
        r_paddle.reset()
        l_paddle.reset()
        turtle.update()
        time.sleep(0.5)
        if l_score.score==6:
            game_on=False
            l_score.soc.clear()
            r_score.soc.clear()
            l_score.win("left")
        elif r_score.score==6:
            game_on=False
            l_score.soc.clear()
            r_score.soc.clear()
            r_score.win("right")
screen.exitonclick()