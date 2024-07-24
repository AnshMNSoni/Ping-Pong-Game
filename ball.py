# Object shape and motion:
from turtle import Turtle, Screen
screen = Screen()

class Object(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('red')
        self.x_move = 15
        self.y_move = 15
          
    def move(self):
        screen.update()
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def y_bounce(self):
        self.y_move *= -1
    
    def x_bounce(self):
        self.x_move *= -1
    
    def reset_position(self):
        self.goto(0, 0)
        self.x_bounce()
        