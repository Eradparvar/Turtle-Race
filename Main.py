from turtle import *
from random import randint
import threading
from MyTurtle import MyTurtle



speed(0)
penup()
goto(-140,140)



for step in range(15):
  write(step, align='center')
  right(90)
  forward(10)
  pendown()
  forward(150)
  penup()
  backward(160)
  left(90)
  forward(20)



# 1st turtle
minnieMouse = MyTurtle('deep sky blue')


minnieMouse.turtle.penup()
minnieMouse.turtle.goto(-160, 100)
minnieMouse.turtle.pendown()

# 2nd turtle
goofy = MyTurtle('lime')

goofy.turtle.penup()
goofy.turtle.goto(-160, 70)
goofy.turtle.pendown()

# 3rd turtle
mickeyMouse = MyTurtle('orchid')

mickeyMouse.turtle.penup()
mickeyMouse.turtle.goto(-160,40)
mickeyMouse.turtle.pendown()

# 4th turtle

donaldDuck = MyTurtle('yellow')

donaldDuck.turtle.penup()
donaldDuck.turtle.goto(-160, 10)
donaldDuck.turtle.pendown()

turtles = [minnieMouse, goofy, mickeyMouse, donaldDuck]

# spins turtle

for index in range(len(turtles)):
    turtles[index].right(360)




for turn in range(100):
    minnieMouse.turtle.forward(randint(1, 5))
    goofy.turtle.forward(randint(1, 5))
    mickeyMouse.turtle.forward(randint(1,5))
    donaldDuck.turtle.forward(randint(1, 5))

def spinTurtle(turtle):

  for turn in range(5):
     turn.turtle.right(72)
