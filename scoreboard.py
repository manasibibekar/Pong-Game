from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score=0
        self.right_score=0
        self.goto(-90,215)
        self.write(self.left_score, align="center", font=("Courier", 55, "normal"))
