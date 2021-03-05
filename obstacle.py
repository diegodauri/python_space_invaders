from turtle import Turtle


class Obstacle(Turtle):
    def __init__(self, position, image):
        super().__init__()
        self.goto(position[0], position[1])
        self.color("white")
        self.shape(image)
        self.penup()

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(y=self.ycor(), x=new_x)

    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(y=self.ycor(), x=new_x)