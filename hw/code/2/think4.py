import math
from swampy.TurtleWorld import *

def drawArc(t, radius, angle):
    length = 2 * math.pi * radius * abs(angle) / 360
    n = int(length / 4) + 1
    step_length = length / n
    step_angle = float(angle) / n
    lt(t, step_angle/2)
    for i in range(n):
        fd(t, step_length)
        lt(t, step_angle)
    rt(t, step_angle/2)
    
def drawPetal(t, radius, angle):
    for i in range(2):
        drawArc(t, radius, angle)
        lt(t, 180-angle)

def drawFlower(t, petals, radius, angle):
    for i in range(petals):
        drawPetal(t, radius, angle)
        lt(t, 360.0/petals)

def drawTriangle(t, length, angle):
    diagLen = length * math.sin(angle * math.pi / 180)
    rt(t, angle)
    fd(t, length)
    lt(t, 90+angle)
    fd(t, 2*diagLen)
    lt(t, 90+angle)
    fd(t, length)
    lt(t, 180-angle) 

def drawPie(t, sides, length):
    angle = 360.0 / sides
    for i in range(sides):
        drawTriangle(t, length, angle/2)
        lt(t, angle)

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

#drawFlower(bob, 7, 60.0, 60.0)
#drawFlower(bob, 10, 40.0, 80.0)
#drawFlower(bob, 20, 140.0, 20.0)

#drawPie(bob, 5, 100)
#drawPie(bob, 6, 100)
#drawPie(bob, 7, 100)

die(bob)
wait_for_user()