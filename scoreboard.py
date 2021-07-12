import time
from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.update_score()
    def increase(self):
        self.score=self.score+1
        self.clear()
        self.update_score()
    def update_score(self):
        self.write(f"score: {self.score}",align="center", font=("Arial", 24,"normal"))
    def game_over(self):
        self.goto(0,0)
        
        self.write("GAME OVER!",align="center", font=("Arial", 24,"normal"))
        
