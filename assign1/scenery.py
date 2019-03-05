"""
This program uses various shapes to draw a scenery containing a house, the sun,
and two trees. Shapes used:
-Rectangle
-Square
-Triangle
-Circle

Author: Aashwin Katiyar
e-mail: ak2577@rit.edu
"""

import turtle as tt
import datetime
import time
import math


def init():
    """
    The initializer function to set the home position for the turtle to start
    drawing
    pre-condition: Turtle is down, facing east
    post-condition: Turtle is up, at the the coordinates, (-150, -150)
    """
    tt.speed(0)
    tt.up()
    tt.back(80)
    tt.right(90)
    tt.forward(200)
    tt.left(90)
    tt.down()
    tt.forward(555)
    tt.back(955)
    tt.up()
    tt.forward(400)


def Square(x):
    """
    Draws a Square
    param x: takes a value for the side
    pre-condition: Turtle is up, facing east
    post-condition: Turtle is up, facing east
    """
    tt.down()
    tt.forward(x)
    tt.left(90)
    tt.forward(x)
    tt.left(90)
    tt.forward(x)
    tt.left(90)
    tt.forward(x)
    tt.left(90)
    tt.up()


def Rectangle(x, y):
    """
    Draws a Rectangle
    param x: takes a value for the length
    param y: takes a value for the bredth
    pre-condition: Turtle is up, facing east
    post-condition: Turtle is up, facing east
    """
    tt.down()
    tt.forward(x)
    tt.left(90)
    tt.forward(y)
    tt.left(90)
    tt.forward(x)
    tt.left(90)
    tt.forward(y)
    tt.left(90)
    tt.up()


def Triangle(x):
    """
    Draws a Triangle
    param x: takes a value for the side
    pre-condition: Turtle is up, facing east
    post-condition: Turtle is up, facing east
    """
    tt.down()
    tt.forward(x)
    tt.left(120)
    tt.forward(x)
    tt.left(120)
    tt.forward(x)
    tt.left(120)
    tt.up()


def Circle(r):
    """
    Draws a Circle
    param r: takes a value for the radius
    pre-condition: Turtle is up, facing east
    post-condition: Turtle is up, facing east
    """
    tt.down()
    tt.circle(r)
    tt.up()


def make_building():
    """
    Draws the basic building base of color blue.
    """
    tt.fillcolor('blue')
    tt.begin_fill()
    Rectangle(160, 210)
    tt.end_fill()


def make_window():
    """
    Draws the window  of color white
    """
    tt.fillcolor('white')
    tt.begin_fill()
    Square(20)
    tt.end_fill()


def make_door():
    """
    Draws the door of color brown
    """
    tt.fillcolor('brown')
    tt.begin_fill()
    Rectangle(40, 60)
    tt.end_fill()


def make_roof():
    """
    Draws the roof of color red
    """
    tt.fillcolor('red')
    tt.begin_fill()
    Triangle(160)
    tt.end_fill()


def make_bark(x, y):
    """
    Draws the bark of the tree of color brown
    param x: The width of rectangle
    param y: The length of rectangle
    """
    tt.fillcolor('brown')
    tt.begin_fill()
    Rectangle(x, y)
    tt.end_fill()


def make_leaves(r):
    """
    Draws the leaves of the tree of color green
    param r: radius of the tree-top
    """
    tt.fillcolor('green')
    tt.begin_fill()
    Circle(r)
    tt.end_fill()


def build_house():
    """
    Draws a house with windows, door and a roof, using rectangles and triangles
    pre-condition: Turtle is up, facing east
    post-condition: Turtle is up, facing east
    """
    make_building()  # Building basic
    tt.forward(60)
    make_door()  # half the size of a door= 20= 80-20 (middle of 160=80)
    tt.left(90)
    tt.forward(170)  # 20 unit margin, goes to 190, 190-20 = 170
    tt.right(90)
    tt.back(40)  # 20 unit margin
    make_window()  # Window
    tt.forward(100)
    make_window()  # Window
    tt.right(90)
    tt.forward(40)
    tt.left(90)
    make_window()  # Window
    tt.back(100)
    make_window()  # Window
    tt.back(20)
    tt.left(90)
    tt.forward(80)
    tt.right(90)
    make_roof()  # Roof
    tt.right(90)
    tt.forward(210)
    tt.left(90)


def build_tree(x, y, r):
    """
    Draws a tree using rectangle and circle
    pre-condition: Turtle is up, facing east
    post-condition: Turtle is up, facing east
    """
    make_bark(x, y)
    tt.left(90)
    tt.forward(y)
    tt.right(90)
    tt.forward(x/2)
    make_leaves(r)
    tt.back(x/2)
    tt.right(90)
    tt.forward(y)
    tt.left(90)


def build_sun():
    """
    builds a sun with a circle of radius 45
    pre-condition: Turtle is up, facing east
    post-condition: Turtle is up, facing east
    """
    tt.fillcolor('yellow')
    tt.begin_fill()
    Circle(45)
    tt.end_fill()


def sun_pos():
    """
    decides the position of sun according to the real life time using the
    module datetime.
    """
    now = datetime.datetime.now()
    h = 160 * (math.sqrt(3)/2)
    if now.hour < 10:
        tt.left(90)
        h = 160 * (math.sqrt(3)/2)
        tt.forward(220+h)
        tt.right(90)
        tt.back(250)
        build_sun()
    elif now.hour >= 10 and now.hour < 2:
        tt.forward(80)
        tt.left(90)
        tt.forward(310+h)
        tt.right(90)
        build_sun()
    elif now.hour > 2:
        tt.left(90)
        h = 160 * (math.sqrt(3)/2)
        tt.forward(220+h)
        tt.right(90)
        tt.forward(440)
        build_sun()


def build_house_and_trees():
    """
    draws house and trees with appropriate spacing between them
    """
    build_house()
    tt.back(90)
    build_tree(10, 120, 60)
    tt.back(140)
    build_tree(10, 120, 70)
    tt.forward(490)
    build_tree(10, 120, 80)
    tt.forward(150)
    build_tree(10, 120, 40)
    tt.back(410)


def build_scenery():
    """
    The ultimate function that calls build_house_and_trees() and sun_pos() to
    draw the whole scenery.
    """
    build_house_and_trees()
    sun_pos()


def main():
    """
    The Main function that calls all other functions to execute the code and
    create a scenery.
    """
    init()
    build_scenery()
    tt.done()


main()
