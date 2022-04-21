#!/usr/bin/env python3
# || ---------- GUI.py ---------- ||
# SHORT DESCRIPTION
# 
# Ben Carpenter
# April 18, 2022
# ------------- GUI.py -------------

from typing import Dict, List
from graphics import GraphWin, GraphicsObject, Entry, Point

from EasyRectangle import EasyRectangle

login_elements= {
    # The items that make up the Login Screen go here
    "passphrase_entry" : Entry(Point(0, 0), 32),
    "login_button": EasyRectangle(Point(250,250), Point(300, 300))
}

read_elements = {
    # The items that make up the Read Screen go here
}

create_elements = {
    # The items that make up the Create Screen go here
}


def open_window() -> GraphWin:
    """Create a new window, and return it"""
    return GraphWin("voice-diary | Ben Carpenter & Nancy Onyimah",500,500)

def close_window(window: GraphWin):
    """Close the window"""
    window.close()

def draw_login(window: GraphWin) -> List[GraphicsObject]:
    """
    Draw the log in field to the window
    """

    # Start by undrawing any current elements:
    for element in read_elements:
        element.undraw(window)

    for element in create_elements:
        element.undraw(window)

    # Draw new elements
    for element in login_elements:
        element.draw(window)


def get_click(window: GraphWin) -> EasyRectangle | None:
    """
    Return what element is clicked to the controller.
    """

    mouse_pos = window.getMouse()

    all_elements = login_elements + read_elements + create_elements

    for element in all_elements:
        if type(element) == EasyRectangle and element.clicked(mouse_pos):
                return element
    
    return None # If the click is not in any of the elements, return None.
