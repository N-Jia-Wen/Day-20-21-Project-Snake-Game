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
        self.show_score()

    def show_score(self):
        self.write(arg=f"Score: {self.score}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.show_score()

    def game_over(self):
        self.teleport(x=0, y=0)
        self.write(arg="GAME OVER", align=ALIGN, font=FONT)
        
