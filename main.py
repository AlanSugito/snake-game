from turtle import Screen
import time
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(key="w", fun=snake.up)
screen.onkey(key="a", fun=snake.left)
screen.onkey(key="s", fun=snake.down)
screen.onkey(key="d", fun=snake.right)


game_is_on = True

while game_is_on:
  screen.update()
  time.sleep(0.1)

  if snake.head.distance(food) < 15:
    food.refresh()
    snake.extend()
    scoreboard.increase_score()
  
  if snake.head.xcor() > 270 or snake.head.xcor() < -270 or snake.head.ycor() > 270 or snake.head.ycor() < -270:
    game_is_on = False
    scoreboard.game_over()
  
  for segment in snake.segments[1:]:
    
    if snake.head.distance(segment) < 10:
      game_is_on = False
      scoreboard.game_over()
  
  snake.move()
  











screen.exitonclick()