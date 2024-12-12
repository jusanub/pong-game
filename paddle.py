from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.right(90)
        self.shapesize(1, 4)
        self.goto(position)

    def move_up(self):
        self.backward(20)
        if self.ycor() > 260:
            self.goto(self.xcor(), 260)

    def move_down(self):
        self.forward(20)
        if self.ycor() < -250:
            self.goto(self.xcor(), -250)