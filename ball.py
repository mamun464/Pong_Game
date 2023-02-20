from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(1,1)
        self.penup()
        self.xMove=10
        self.yMove=10
        self.Bspeed=0.1
        self.speed(self.Bspeed)

    def ball_move(self):
        x = self.xcor() + self.xMove
        y = self.ycor() + self.yMove
        self.goto(x,y)


    def bounce_y(self):
        self.yMove *=-1
    def bounce_x(self):
        self.xMove *=-1
        self.Bspeed *=0.9


    def reset_possition(self):
        self.goto(0,0)
        self.Bspeed=.1
        self.bounce_x()


