from turtle import Turtle

class Over(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("red")

    def end_of_game(self):
        self.write(f"GAME OVER", font=("gothic", 60, "normal"), align="center")