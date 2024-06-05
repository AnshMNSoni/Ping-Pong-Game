from turtle import Turtle
FONT = ('Courier', 42, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        
        # screen.clearscreen()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(-50, 300)
        self.write(f"{self.l_score} {self.r_score}", font=FONT)
        self.pendown()
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.goto(-50, 300)
        self.write(f"{self.l_score} {self.r_score}", font=FONT)
    
    def l_point(self):
        self.l_score += 1
    
    def r_point(self):
        self.r_score += 1