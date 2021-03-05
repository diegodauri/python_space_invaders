from turtle import Turtle

INITIAL_BALL_SIZE = 20
BALL_WIDTH = 10
BALL_HEIGHT = 5
INITIAL_POS_X = 0


class Laser(Turtle):
    def __init__(self, starting_pos, direction):
        super().__init__()
        self.starting_pos = starting_pos
        self.direction = direction
        self.shape("square")
        self.shapesize(stretch_wid=BALL_HEIGHT / INITIAL_BALL_SIZE, stretch_len=BALL_WIDTH / INITIAL_BALL_SIZE)
        self.fillcolor("white")
        self.penup()
        self.initialise_laser()
        self.new_heading = self.heading()
        self.speed("fastest")

    def initialise_laser(self):
        self.goto(x=self.starting_pos[0], y=self.starting_pos[1])
        # Set direction of laser travel
        if self.direction == "Up":
            self.new_heading = 90
        else:
            # Down
            self.new_heading = 270
        self.setheading(self.new_heading)

    def move_laser(self, speed):
        self.forward(speed)

