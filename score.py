from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0,270)
        self.score = 0
        with open("data.txt",mode = "r") as data:
            self.high_score = int(data.read())

        self.update_score()
    def update_score(self):
        self.clear()
        self.write(f"Score:{self.score}    High score{self.high_score}",align = "center",font=("Courier",20,"bold"))


    def count(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()
    # def game_over(self):
    #
    #     self.goto(0,0)
    #     self.write(f"GAME OVER !!!", align="center", font=("Courier", 20, "bold"))
    #
