from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score import Score
import time

# create screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

# create snake, food and score
snake = Snake()
food = Food()
score = Score()

# keyboard movements
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# game
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
   
    snake.move()
    
    # detect colision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increas_score()
        
    # detect colision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()
        
    # detect colision with tail:
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()
            
screen.exitonclick()