from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen= Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("The Pong Game")
screen.tracer(0)

right_paddle=Paddle((350,0))
left_paddle=Paddle((-350,0))
ball = Ball()
scoreboard=ScoreBoard()

screen.listen()
screen.onkey(right_paddle.go_up,"Up")
screen.onkey(right_paddle.go_down,"Down")
screen.onkey(left_paddle.go_up,"w")
screen.onkey(left_paddle.go_down,"s")

game_is_on=True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # detect collision with wall 
    if ball.ycor()>280 or ball.xcor()<-280:
        ball.ybounce()

    # detect collision with paddles.
    if ball.distance(right_paddle)<50 and ball.xcor()>320 or ball.distance(left_paddle)<50 and ball.xcor()<-320:
        ball.xbounce()

    # detect when right paddle misses
    if ball.xcor()>380:
        ball.reset_position()
    
    # detect when left paddle misses
    if ball.xcor()<-380:
        ball.reset_position()

screen.exitonclick()