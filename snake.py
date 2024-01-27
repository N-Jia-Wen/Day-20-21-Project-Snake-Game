from turtle import Turtle
STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        # (Length refers to how many segments the snake starts out with)
        self.segment_list = []
        self.create_snake()
        self.head = self.segment_list[0]

    # Creates the starting body of the snake. Occurs when object is created
    def create_snake(self):
        for position in STARTING_POS:
            self.add_segment(position)
    # Can also loop through a list containing tuples with the coordinates, but snake length will be constant

    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segment_list.append(segment)

    def extend(self):
        self.add_segment(self.segment_list[-1].position())

    def move(self):
        for seg_no in range(len(self.segment_list) - 1, 0, -1):
            new_x = self.segment_list[seg_no - 1].xcor()
            new_y = self.segment_list[seg_no - 1].ycor()
            self.segment_list[seg_no].goto(new_x, new_y)
        self.head.forward(MOVE_DIST)

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
