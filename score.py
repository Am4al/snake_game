from turtle import Turtle
ALIGN = 'center'
FONT = ('Arial', 24, 'normal')

class ScoreBord(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.up_score()

    def up_score(self):
        self.write(f"Score: {self.score}", align=ALIGN,
                   font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN,
                   font=FONT)

    def inc_score(self):
        self.score += 1
        self.clear()
        self.up_score()