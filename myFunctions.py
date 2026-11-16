import turtle
bob=turtle.Turtle()

def jump(x,y):
  bob.penup()
  bob.goto(x,y)
  bob.pendown()

def toom_bluey_flare(c):
  for times in range(140):
    bob.circle(times + 50)
    bob.left(times + 90)
    bob.circle(times + 50)
    bob.right(times + 180)
      
def square(sides,distance,color,width):
    bob.pencolor("white")
    angle = 360/sides
    for times in range(sides):
      bob.forward(distance)
      bob.left(angle)

def triangular_like_spiral():
  for number in range(40):
    bob.forward(number * 4)
    bob.left(120)

def circle(radius, border_color, fill_color):
  bob.pencolor(border_color)
  bob.fillcolor(fill_color)
  bob.begin_fill()
  bob.circle(radius)
  bob.end_fill()
