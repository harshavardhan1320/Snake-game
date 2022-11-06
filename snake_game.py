from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import ScoreBoard

s = Screen()

s.setup(width=600, height=600)
s.bgcolor("black")
s.title("My Snake Game")
s.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()


s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    s.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        score.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if segment == snake.head:
            pass

        elif snake.head.distance(segment) < 9:
            score.reset()
            snake.reset()


s.exitonclick()
