from turtle import *

import self as self


class MyTurtle:

    def __init__(self, color):
        self.turtle = Turtle()
        self.turtle.color(color)
        self.turtle.shape('turtle')

    def turtle(self):
        return self.turtle

    def right(self, angles):
        self.turtle.right(angles)
