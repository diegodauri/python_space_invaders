from turtle import Turtle


class Player(Turtle):

    def __init__(self, position, image):
        super().__init__()
        self.shape(image)
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(position)

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(y=self.ycor(), x=new_x)

    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(y=self.ycor(), x=new_x)
