# Project need functions to call and define, loops, random #, colors, backround color, circles(full,and arc), set heading, width 

from myFunctions import *
from random import *

turtle.tracer(0)

turtle.colormode(255)
turtle.bgcolor("black")

# spiral triangles
jump(500,200)
bob.pencolor("white")
for number in range(40):
    bob.width(2)
    bob.forward(number * 4)
    bob.left(120)

jump(-500,200)
bob.pencolor("white")
for number in range(40):
    bob.width(2)
    bob.forward(number * 4)
    bob.left(120)

jump(500,-200)
bob.pencolor("white")
for number in range(40):
    bob.width(2)
    bob.forward(number * 4)
    bob.left(120)

jump(-500,-200)
bob.pencolor("white")
for number in range(40):
    bob.width(2)
    bob.forward(number * 4)
    bob.left(120)

# nice toom blue desgin loop of some sort
jump(0,0)
bob.width(1)
c = (112,134,200)
bob.pencolor(c)
toom_bluey_flare(c)

# random number of circles they are
num = randint(20, 75)

for times in range( num ):
  r = randint(255, 255)
  g = randint(0, 0)
  b = randint(0, 0)
  border = "red"
  fill = (r,g,b)
  x = randint(-350, 350)
  y = randint(-350, 350)
  radius = randint(10, 10)
  circle(20, "red", "red" )
  jump(x,y)

# my desgin is called Hyper Cool
