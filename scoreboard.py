from turtle import Turtle
FONT = ("Courier", 20, "normal")
ALIGN = 'center'


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-250, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'LEVEL: {self.level}', align=ALIGN, font=FONT)

    def increase_score(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align=ALIGN, font=FONT)
        

    
