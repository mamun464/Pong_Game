from turtle import Turtle


class Paddle(Turtle):
    
    def __init__(self,x,y):
        super().__init__()
        self.shape("square")
        self.color("White")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.pu()
        self.goto(x, y)

    def go_up(self):
        new_y = self.ycor() + 20

        if new_y < 270:
         self.goto(x=self.xcor(), y=new_y)


    def go_down(self):
        new_y = self.ycor() - 20

        if new_y > -270:
         self.goto(x=self.xcor(), y=new_y)
