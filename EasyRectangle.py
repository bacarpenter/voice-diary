#!/usr/bin/env python3
# || ---------- EasyRectangle.py ---------- ||
# Originaly authored by Prof. Johanna Brewer
# and updated hevily by Ben Carpenter and
# Nancy Onyimah
# 
# Ben Carpenter and Nancy Onyimah
# April 24, 2022
# ------------- EasyRectangle.py -------------


from graphics import Rectangle, Point

# EasyRectangles are defined by x,y center coordiantes, width, and height
# They can detect if a given point lies inside of themselves

class EasyRectangle(Rectangle):
    # Creates rectangle object of specified width and height
    # centered on point at (x_center,y_center) 
    def __init__(self, top_left, bottom_right):
        super().__init__(top_left,bottom_right)

    # Returns true if the point lies within rectangle, and the rectangle is drawn
    def clicked(self, point):
        return self.getP1().getX() <= point.getX() <= self.getP2().getX() and self.getP1().getY() <= point.getY() <= self.getP2().getY() and self.canvas != None
