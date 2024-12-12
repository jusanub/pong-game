from turtle import Screen
from scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle

screen = Screen()
screen.bgcolor('black')
screen.setup(800, 600)
screen.tracer(0)

player_1 = Paddle((350, 0))
player_2 = Paddle((-350, 0))
ball = Ball()
player2_score = Scoreboard((-200, 270))
player1_score = Scoreboard((200, 270))

screen.listen()

screen.onkey(player_1.move_up, 'Up')
screen.onkey(player_1.move_down, 'Down')
screen.onkey(player_2.move_up, 'w')
screen.onkey(player_2.move_down, 's')


game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    ball.bounce_on_wall()

    if ball.xcor() <= -390:
        player1_score.increase_score()
        ball.goto(0, 0)
        ball.bounce_x()

    if ball.xcor() >= 390:
        player2_score.increase_score()
        ball.goto(0, 0)
        ball.bounce_x()

    if ball.distance(player_1) < 40 and ball.xcor() > 330:
        player1_score.increase_score()
        ball.bounce_x()

    if ball.distance(player_2) < 40 and ball.xcor() < -330:
        player2_score.increase_score()
        ball.bounce_x()

screen.exitonclick()