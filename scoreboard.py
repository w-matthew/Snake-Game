from turtle import Turtle
STYLE = ("Courier", 14)
ALIGNMENT = "Center"
TEXT_SET = (0, 270)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.curr_score = 0
        self.show()

    def add_score(self):
        self.curr_score += 1

    def show(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(TEXT_SET)
        self.color("white")
        self.write(f"Score = {self.curr_score}", font=STYLE, align=ALIGNMENT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=STYLE)
