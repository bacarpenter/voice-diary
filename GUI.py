#!/usr/bin/env python3
# || ---------- GUI.py ---------- ||
# SHORT DESCRIPTION
# 
# Ben Carpenter
# April 18, 2022
# ------------- GUI.py -------------

# https://realpython.com/iterate-through-dictionary-python/

from graphics import GraphWin, GraphicsObject, Entry, Point, Circle, Text, color_rgb

from EasyRectangle import EasyRectangle
from Entry_Button import EntryButton

mic_button = EasyRectangle(Point(210,210), Point(290, 290))
mic_button.setFill(color_rgb(166, 112, 169))

welcome_text = Text(Point(250,100), "Voice Diary")
welcome_text.setSize(24)
welcome_text.setStyle("bold")
welcome_text.setFace("times roman")
welcome_text.setTextColor(color_rgb(166, 112, 169))

login_text = Text(Point(250,400), "Please speak your passphrase!")
login_text.setSize(18)
login_text.setStyle("bold")
login_text.setFace("times roman")
login_text.setTextColor(color_rgb(166, 112, 169))

login_elements= {
    # The items that make up the Login Screen go here
    "welcome_text": welcome_text,
    "login_button": mic_button,
    "instruction_text": login_text,
}


entries_text = Text(Point(100,50), "Entries")
entries_text.setSize(24)
entries_text.setStyle("bold")
entries_text.setFace("times roman")
entries_text.setTextColor(color_rgb(166, 112, 169))

read_elements = {
    # The items that make up the Read Screen go here
    "entries_text": entries_text
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

def draw_login(window: GraphWin):
    """
    Draw the log in field to the window
    """

    # Start by undrawing any current elements:
    for element in read_elements:
        read_elements[element].undraw()

    for element in create_elements:
        create_elements[element].undraw()

    # Draw new elements
    for element in login_elements:
        login_elements[element].draw(window)


def draw_read(window: GraphWin):
    e = EntryButton(Point(25, 75), "Title", "Body text", 14)
    e.draw(window)

    for element in create_elements:
        create_elements[element].undraw()

    for element in login_elements:
        login_elements[element].undraw()

    for element in read_elements:
        read_elements[element].draw(window)

def get_click(window: GraphWin) -> EasyRectangle | None:
    """
    Return what element is clicked to the controller.
    """

    mouse_pos = window.getMouse()

    all_elements = {**login_elements, **create_elements, **read_elements}
    for element in all_elements:
        if type(all_elements[element]) == EasyRectangle:
            if all_elements[element].clicked(mouse_pos):
                return element
        elif type(all_elements[element] == EntryButton):
            if all_elements[element].go_button.clicked(mouse_pos):
                return all_elements[element].id
    
    return None # If the click is not in any of the elements, return None.
