import time
from turtle import Turtle, Screen
from snakes import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(600, 600)
screen.title("My Snake game ")
screen.tracer(0)
screen.bgcolor("black")


#create snake
snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Dtetect collision with food
    if snake.head.distance(food)<15:
        snake.extend()
        print("nom nom nom")
        food.refresh()
        scoreboard.increase_score()

    #DETECT COLLISION WITH WALL
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor() > 290 or snake.head.ycor()< -290:
        scoreboard.reset()
        snake.reset()

    #detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<15:
            scoreboard.reset()

    #if head collides with any segment in the tail:


screen.exitonclick()