from turtle import Turtle


class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.goto(0, 270)
        self.color("white")
        self.write(f"{self.left_score} : {self.right_score}", move=False, align="center", font=("Arial", 22, "normal"))
        self.hideturtle()
        
        

    def left_increase(self):
        self.left_score = self.left_score + 1
        self.clear()
        self.write(f"{self.left_score} : {self.right_score}", move=False, align="center", font=("Arial", 22, "normal"))


    def right_increase(self):
        self.right_score = self.right_score + 1
        self.clear()
        self.write(f"{self.left_score} : {self.right_score}", move=False, align="center", font=("Arial", 22, "normal"))