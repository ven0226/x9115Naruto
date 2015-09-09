"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

import math

try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *


def square(t, length):
    """Draws a square with sides of the given length.

    Returns the Turtle to the starting position and location.
    """
    for i in range(4):
        fd(t, length)
        lt(t)


def polyline(t, n, length, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        fd(t, length)
        lt(t, angle)


def polygon(t, n, length):
    """Draws a polygon with n sides.

    t: Turtle
    n: number of sides
    length: length of each side.
    """
    angle = 360.0/n
    polyline(t, n, length, angle)


def arc(turtleParam, r, angle):

    arclen = 2 * math.pi * r * angle / 360
    n = int(arclen / 4) + 1
    steplen = arclen / n
    stepangle = float(angle) / n

    for i in range(n):
        fd(turtleParam, steplen)
        lt(turtleParam, stepangle)



def circle(t, r):
    """Draws a circle with the given radius.

    t: Turtle
    r: radius
    """
    arc(t, r, 360)


# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.

if __name__ == '__main__':
    world = TurtleWorld()

    bob = Turtle()
    bob.delay = 0.001

    arc(bob,50,90)
    lt(bob, 90)
    lt(bob, 360/1)

    arc(bob,50,90)
    lt(bob, 90)
    lt(bob, 360/2)

    arc(bob,50,90)
    lt(bob, 90)
    lt(bob, 360/3)

    arc(bob,50,90)
    lt(bob, 90)
    lt(bob, 360/4)

    # draw a circle centered on the origin
    '''
    fd(bob, 100)
    lt(bob)
    fd(bob, 100)
    radius = 100
    pu(bob)
    fd(bob, radius)
    lt(bob)
    pd(bob)
    circle(bob, radius)
    '''
    wait_for_user()
