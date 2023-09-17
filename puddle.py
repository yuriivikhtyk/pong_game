from turtle import Turtle

class Puddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.penup()
        self.start_x = 350
        self.start_y = 0
        self.shapesize(5, 1)
        self.goto(x, y)
        self.color("white") 
        

    def up(self):
        self.goto(self.xcor(), self.ycor()+20)


    def down(self):
        self.goto(self.xcor(), self.ycor()-20)
        