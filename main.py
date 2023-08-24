# Turtle Party Project
# By Wai Yau
# 08.23.23

import turtle
turtle.color("red")

size = 100
# Reapeat 3 times
def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()

def triangle(size):
  for i in range(4):
    turtle.forward(size)
    turtle.left(90)  

def move(angle, length):
  turtle.penup()
  turtle.left(angle)
  turtle.forward(length)
  turtle.pendown()
    
def polyon(sides,length):
  angle = 360 / sides
  for i in range(sides):
    turtle.forward(length/sides)
    turtle.left(angle)

def spiral(len, angle):
  for i in range(20):
    turtle.forward(len)
    turtle.left(angle)
    len += 5

spiral(4,120)

# len = 100    
# for i in range(3,10):
#   angle = 360/i
#   polyon(i,len)
#   move(angle, len)
    
# triangle(100)
# back(75)
# triangle(50)
# back(50)
# triangle(25)
