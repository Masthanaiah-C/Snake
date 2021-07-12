from scoreboard import Score
from food import Food
import turtle
import time
import snake
screen = turtle.Screen()
screen.setup(width=600,height=600)
screen.title("my snake game")
screen.tracer(0)


s= snake.Snake()
f = Food()
score = Score()
screen.listen()
screen.onkey(s.up,"Up")
screen.onkey(s.down,"Down")
screen.onkey(s.left,"Left")
screen.onkey(s.right,"Right")
game_on = True
turn = 0
while(game_on):
    s.move()
    
    time.sleep(0.1)
    screen.update()
    if s.head.distance(f)<15:
        f.refresh()
        score.increase()
        s.extend()
    if s.head.xcor() >280 or s.head.xcor() <-280 or s.head.ycor() >280 or s.head.ycor() <-280 :
        game_on = False
        score.game_over()
    for seg in s.segments[1:]:
        if seg == s.head:
            pass
        elif snake.head.distance(seg) <10 :
            game_on=False
            score.game_over()    
    
    
    
    
screen.exitonclick()