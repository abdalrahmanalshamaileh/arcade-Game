#1 using turtle library to built the opponents 
#2 using calss ball 
#3 class for the score board 
#4 class for the players to locate the ball from side to side 

from turtle import Turtle,Screen
from paddle import Paddl
from ball import Ball
import time
from score import Score

screen=Screen()
screen.setup(height=600,width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
ball=Ball()


s=Score()
r_paddle=Paddl((350,0))
l_paddle=Paddl((-350,0))


screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeyrelease(r_paddle.stop_move, "Up")  # Stop paddle movement when key is released
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeyrelease(r_paddle.stop_move, "Down")  # Stop paddle movement when key is released

screen.onkeypress(l_paddle.go_up, "w")
screen.onkeyrelease(l_paddle.stop_move, "w")  # Stop paddle movement when key is released
screen.onkeypress(l_paddle.go_down, "s")
screen.onkeyrelease(l_paddle.stop_move, "s")  # Stop paddle movement when key is released


game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    # Detect the collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect when r_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        s.l_point()

    # Detect when L_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()  # You missed the function call here
        s.r_point()  # You missed the function call here

screen.exitonclick()
