from turtle import *
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITION = ((20,0),(0,0),(-20,0))
class Snack():

    direction=[20,0,-20]
    def __init__(self):
        self.segment = []
        self.create_snack()
        self.head = self.segment[0]
    def create_snack(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self ,position):
            snack = Turtle()
            snack.penup()
            snack.shape("square")
            snack.color("white")
            snack.goto(position)
            self.segment.append(snack)

    def  extend(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
         for seg in range(len(self.segment)-1,0,-1):
                nex_x = self.segment[seg -1].xcor()
                nex_y = self.segment[seg - 1].ycor()
                self.segment[seg].goto(nex_x,nex_y)
         self.segment[0].forward(15)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)