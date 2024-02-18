from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.count = 0
        with open("data.txt") as file:
            self.high_score = file.read()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.update_scoreboard()

    def score(self):
        self.count += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.count} High Score: {self.high_score}", False, "center", ("Courier", 12, "normal"))

    def reset(self):
        if self.count > int(self.high_score):
            self.high_score = self.count
        self.count = 0
        self.update_scoreboard()
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))




