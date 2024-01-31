from turtle import Turtle
ALIGN = "center"
FONT = ("Press Start 2P", 16, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.teleport(x=0, y=280)
        self.score = 0
        with open(file="data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.show_score()

# New method added: replaced game_over() with reset()
    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(file="data.txt", mode="w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.show_score()
