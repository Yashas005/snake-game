from turtle import Turtle

positions=[(0,0),(-20,0),(-40,0)]
move_distance = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in positions:
            self.add_segment(position)

    def add_segment(self,position):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
        self.segments[0].shape("triangle")



    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)

        self.segments[0].forward(move_distance)

    def up(self):
        if self.segments[0].heading()!=DOWN:
           self.segments[0].setheading(UP)

    def down(self):
       if self.segments[0].heading()!=UP:
          self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading()!=RIGHT:
           self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading()!=LEFT:
           self.segments[0].setheading(0)
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()


