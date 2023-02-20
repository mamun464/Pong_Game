from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score=0
        self.r_score = 0
        self.r_miss=5
        self.l_miss = 5
        self.color("white")
        self.hideturtle()
        self.pu()
        self.up_scoreBoard()

    def up_scoreBoard(self):
        self.clear()
        self.goto(-150, 265)
        self.write(f" Score: {self.l_score}", align='center', font=('courier', 15, 'normal'))
        self.goto(260, 265)
        self.write(f" Score: {self.r_score}", align='center', font=('courier', 15, 'normal'))

        self.goto(150, 265)
        self.write(f"Life: {self.r_miss} |", align='center', font=('courier', 15, 'normal'))
        self.goto(-260, 265)
        self.write(f"Life: {self.l_miss} |", align='center', font=('courier', 15, 'normal'))





    def l_point(self):
            self.l_score +=1

            self.r_life()
            self.up_scoreBoard()

    def r_point(self):
            self.r_score +=1

            self.l_life()
            self.up_scoreBoard()


    def r_life(self):
            self.r_miss -= 1
            self.up_scoreBoard()

    def l_life(self):
            self.l_miss -= 1
            self.up_scoreBoard()

    def gameOver(self):
        self.goto(0, 0)

        self.write(arg=f"GAME OVER!", align='center', font=('courier', 20, 'normal'))
