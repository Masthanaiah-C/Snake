import turtle
Up=90.0
Down=270.0
Right=0.0
Left=180.0
initial_positions = [(0,0),(0,-20),(0,-40)]
move_distance = 20
import time
class Snake:
    def __init__(self):

        self.segments = []
        self.create_snake()
        self.head=self.segments[0]
    def create_snake(self):
        for position in initial_positions:
            segment=turtle.Turtle("square")
            segment.color('black')
            
            segment.penup()
            segment.left(90)
            segment.goto(position)
            self.segments.append(segment)
    def move(self):
        for seg in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg-1].xcor()
            new_y = self.segments[seg-1].ycor()
            self.segments[seg].goto(new_x,new_y)
        self.head.forward(move_distance)
    def up(self):
       
        if((self.head.heading())!=Down): 
            self.head.setheading(Up)

    def down(self):
        if(self.head.heading()!=Up): 
            self.head.setheading(Down)
    def right(self):
        if(self.head.heading()!=Left): 
            self.head.setheading(Right)
    def left(self):
        if(self.head.heading()!=Right): 
            self.head.setheading(Left)
    def extend(self):
        segment=turtle.Turtle("square")
        segment.color('black')
        segment.penup()
        new_x = self.segments[-1].xcor()
        new_y = self.segments[-1].ycor()
        self.segments.append(segment)
        self.segments[-1].goto(new_x,new_y)
        
        
        
        
