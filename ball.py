from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.shapesize(.7)
        self.penup()
        self.x = 2
        self.y = 2

    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y *= -1

    def bounce_x(self):
        self.x *= -1

    def bounce_on_wall(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.bounce_y()
