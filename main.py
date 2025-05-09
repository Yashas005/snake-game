from turtle import Screen
from snake import Snake
from food import Food
from score import Score

import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake game !")
screen.tracer(0)
snake = Snake()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
food = Food()
segments = []
score = Score()


gameon = True

while gameon:
    screen.update()
    time.sleep(0.1)
    snake.move()



    if snake.segments[0].distance(food)<15:
        score.count()
        food.refresh()
        snake.extend()
    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() < -290 or snake.segments[0].ycor() > 290:
        score.reset()
        snake.reset()

    # to detect collisions
    for segment in snake.segments[1:]:
        if segment == snake.segments[0]:
            pass
        elif snake.segments[0].distance(segment) < 10:
            score.reset()
            snake.reset()

















screen.exitonclick()
