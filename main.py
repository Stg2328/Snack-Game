import time
from turtle import Turtle,Screen
from snack import Snack
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(610,610)
screen.bgcolor("black")
screen.title("Stg's Snack Game")
screen.tracer(0)

snack = Snack()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snack.up,"Up")
screen.onkey(snack.down,"Down")
screen.onkey(snack.left,"Left")
screen.onkey(snack.right,"Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snack.move()
    if snack.head.distance(food) < 15:
        food.refresh()
        snack.extend()
        scoreboard.increace_score()

    if snack.head.xcor() > 280 or  snack.head.xcor() < -280 or snack.head.ycor() > 280 or snack.head.ycor() < -280 :
        game_on = False
        scoreboard.game_over()
    for segment in snack.segment[1:]:
        if snack.head.distance(segment) < 10 :
            game_on = False
            scoreboard.game_over()



screen.exitonclick()