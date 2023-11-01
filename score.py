from turtle import Screen, Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
    
    def update_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=("Arial", 24, "normal"))


    def increas_score(self):
        self.clear()
        self.score += 1
        self.update_score()
        
            
            