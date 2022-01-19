from turtle import Turtle
STYLE = ("Courier", 14)
ALIGNMENT = "Center"
TEXT_SET = (0, 270)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as file:
            self.high_score = int(file.read())
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
        self.write(f"Score = {self.curr_score} High Score: {self.high_score}", font=STYLE, align=ALIGNMENT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=STYLE)

    def reset_game(self):
        if self.curr_score > self.high_score:
            self.high_score = self.curr_score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.curr_score}")

            self.curr_score = 0

