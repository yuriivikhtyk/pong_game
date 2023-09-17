from turtle import Turtle, Screen
from puddle import Puddle
from ball import Ball
import time
from score import Score


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.listen()
screen.tracer(0)


pud_r = Puddle(350, 0)
pud_l = Puddle(-350, 0)
score = Score()
screen.onkey(pud_r.up, 'Up')
screen.onkey(pud_r.down, 'Down')
screen.onkey(pud_l.up, 'w')
screen.onkey(pud_l.down, 's')
ball = Ball()

game_is_on = True

while game_is_on:
    ball.general_movement()
    screen.update()
    time.sleep(ball.move_speed)
    
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce()
        
    if ball.distance(pud_r) < 50 and ball.xcor() > 320 or  ball.distance(pud_l) < 50 and ball.xcor() < -320:
        ball.contact()

        

    if ball.xcor() < -380:
        score.right_increase()
        ball.restart()

    if ball.xcor() > 380:
        score.left_increase()
        ball.restart()




screen.exitonclick()