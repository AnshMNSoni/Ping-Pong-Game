from turtle import Turtle, Screen

LEFT_POSITION = [(-450, 300), (-450, 280), (-450, 260), (-450, 240)]
RIGHT_POSITION = [(450, 300), (450, 280), (450, 260), (450, 240)]
screen = Screen()

class LeftReflector:
    def __init__(self):
        self.segments = []
        self.create_reflector()
        
    def create_reflector(self):
        for seg in LEFT_POSITION:
            new_turtle = Turtle('square')
            new_turtle.penup()
            new_turtle.color('white')  
            new_turtle.goto(seg)  
            self.segments.append(new_turtle)
        screen.update()
            
    def down(self):
        self.segments[3].setheading(270)
        for turtles in range(len(self.segments) - 1):
            x = self.segments[turtles + 1].xcor()
            y = self.segments[turtles + 1].ycor()
            self.segments[turtles].goto(x, y)
        self.segments[3].fd(20)
        screen.update() 
    
    def up(self):
        self.segments[0].setheading(90)
        for turtles in range(len(self.segments) - 1, 0, -1):
            x = self.segments[turtles - 1].xcor()
            y = self.segments[turtles - 1].ycor()
            self.segments[turtles].goto(x, y)
        self.segments[0].fd(20)
        screen.update()

class RightReflector(LeftReflector):
    def __init__(self):
        self.segments = []
        self.create_reflector()
        
    def create_reflector(self):
        for seg in RIGHT_POSITION:
            new_turtle = Turtle('square')
            new_turtle.penup()
            new_turtle.color('white')  
            new_turtle.goto(seg)  
            self.segments.append(new_turtle)
        screen.update()
        
    def up(self):
        super().up()
    
    def down(self):
        super().down()
        
    