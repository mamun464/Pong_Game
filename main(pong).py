import time
from turtle import Turtle,Screen
from scoreboard import ScoreBoard

from ball import Ball
from paddle import Paddle



screen=Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=800,height=600)
screen.tracer(0)


screen.listen()

r_paddle=Paddle(350,0)
l_paddle=Paddle(-350,0)
ball= Ball()
scoreboard=ScoreBoard()

screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeypress(r_paddle.go_down,"Down")
screen.onkeypress(l_paddle.go_up,"w")
screen.onkeypress(l_paddle.go_down,"s")



game_star=True
while game_star:
    time.sleep(ball.Bspeed)
    screen.update()
    ball.ball_move()


    #dectech with wall colission
    if ball.ycor()>=289 or  ball.ycor()<=-289:
        ball.bounce_y()

    #detect with Right paddle colission

    if ball.distance(r_paddle)<=50 and ball.xcor() > 320 or ball.distance(l_paddle)<=50 and ball.xcor() < -320:
        ball.bounce_x()


    #ball miss the right paddle
    if ball.xcor()>380:
        ball.reset_possition()
        scoreboard.l_point()



        # ball miss the left paddle
    if ball.xcor() < -380:
        ball.reset_possition()
        scoreboard.r_point()


    if scoreboard.r_miss <= 0:
        scoreboard.gameOver()
        game_star = False
    if scoreboard.l_miss <= 0:
        scoreboard.gameOver()
        game_star=False



screen.exitonclick()