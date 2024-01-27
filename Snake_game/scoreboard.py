from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.count = 0

    def score(self):
        self.count += 1
        self.clear()
        return self.count

    def show_score(self, x):
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.write(f"Score: {x}", False, "center", ("Courier", 12, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center",("Courier", 15, "normal"))
