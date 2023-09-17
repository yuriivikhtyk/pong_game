from turtle import Turtle
import random
DIRECTIONS = [1, -1]


class Ball(Turtle):
    x_randomiser = random.choice(DIRECTIONS)
    y_randomiser = random.choice(DIRECTIONS)
    move_speed = 0.2

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.x_move = self.x_randomiser*13
        self.y_move = self.y_randomiser*13
        

    def general_movement(self):
        self.goto(self.xcor()+self.x_move, self.ycor()+self.y_move)


    def bounce(self):
        self.y_move = self.y_move * (-1)
        self.move_speed *= 0.9


    def contact(self):
        self.x_move = self.x_move * (-1)


    def restart(self):
        self.goto(0,0)
        self.contact()
        self.move_speed = 0.2
        