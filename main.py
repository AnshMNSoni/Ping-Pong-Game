from turtle import Screen, Turtle
from reflector import LeftReflector, RightReflector
from ball import Object
from scoretrack import Score
import time

tt = Turtle()
screen = Screen()
screen.title('PING-PONG Game')
screen.bgcolor('black')
screen.setup(height=750, width=950)

# Turtle tracer is off:
screen.tracer(0)
tt.goto(0, 350)
tt.hideturtle()
tt.color('white')
tt.right(90)
tt.pensize(5)
while True:
    tt.fd(20)
    tt.penup()
    tt.fd(20)
    tt.pendown()
   
    if (tt.ycor() <= -370):
        break
    
    
left = LeftReflector()
right = RightReflector()
        
screen.listen()
screen.onkey(key='w', fun=left.up)
screen.onkey(key='s', fun=left.down)
screen.onkey(key='Up', fun=right.up)
screen.onkey(key='Down', fun=right.down)
    
# Score Track:
scoreboard = Score()

# Ball Track:
object = Object()  


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    object.move()
    
    # collision with reflector:
    for seg_lst in range(4):
        if (abs(object.ycor()) >= 350):
            object.y_bounce()
            object.move()
        
        if (object.xcor() >= 480):
            scoreboard.l_point()
            scoreboard.update_score()
            object.reset_position()
        
        if (object.xcor() <= -480):
            scoreboard.r_point()
            scoreboard.update_score()
            object.reset_position()
            
        if (right.segments[seg_lst].distance(object) <= 25):
            object.x_bounce()
            object.move()
        
        if (left.segments[seg_lst].distance(object) <= 25):
            object.x_bounce()
            object.move()

screen.update()
screen.exitonclick()