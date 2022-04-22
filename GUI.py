#!/usr/bin/env python3
# || ---------- GUI.py ---------- ||
# SHORT DESCRIPTION
# 
# Ben Carpenter
# April 18, 2022
# ------------- GUI.py -------------

# https://realpython.com/iterate-through-dictionary-python/

import re
from graphics import GraphWin, GraphicsObject, Entry, Point, Circle, Text, color_rgb
import entry

from EasyRectangle import EasyRectangle
from Entry_Button import EntryButton
from typing import List

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

page_text = Text(Point(250, 480), "X - X")
page_down_button = EasyRectangle(Point(200, 470), Point(220, 490))
page_down_text = Text(Point(210, 480), "←")
page_up_button = EasyRectangle(Point(280, 470), Point(300, 490))
page_up_text = Text(Point(290, 480), "→")

logout_button = EasyRectangle(Point(150, 470), Point(170, 490))
logout_text = Text(Point(160, 480), "Log\nOut")
logout_text.setSize(8)

create_button = EasyRectangle(Point(330, 470), Point(350, 490))
create_text = Text(Point(340, 480), "New")
create_text.setSize(8)

read_elements = {
    # The items that make up the Read Screen go here
    "entries_text": entries_text,
    "page_text": page_text,
    "page_down": page_down_button,
    "page_down_text": page_down_text,
    "page_up": page_up_button,
    "page_up_text": page_up_text,
    "logout": logout_button,
    "logout_text": logout_text,
    "create": create_button,
    "create_text": create_text
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


def draw_read(window: GraphWin, entries: List[entry.Entry], page_start: int, page_end: int):
    # Add entry elements to the element list
    global read_elements

    entry_elements = {}
    top_left_y = 75

    for element in read_elements:
        read_elements[element].undraw()

    read_elements = {
        # The items that make up the Read Screen go here
        "entries_text": entries_text,
        "page_text": page_text,
        "page_down": page_down_button,
        "page_down_text": page_down_text,
        "page_up": page_up_button,
        "page_up_text": page_up_text,
        "logout": logout_button,
        "logout_text": logout_text,
        "create": create_button,
        "create_text": create_text
    }

    if page_end > len(entries): page_end = len(entries)
    
    for entry in entries[page_start - 1: page_end-1]:
        entry_elements.update({entry.id: EntryButton(Point(25, top_left_y), entry.title, entry.text)}),
        top_left_y += 60

    read_elements.update(entry_elements) # https://www.programiz.com/python-programming/methods/dictionary/update


    for element in login_elements:
        login_elements[element].undraw()

    read_elements['page_text'].setText(f"{page_start} - {page_end}")

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
        elif type(all_elements[element]) == EntryButton:
            if all_elements[element].go_button.clicked(mouse_pos):
                return element
    
    return None # If the click is not in any of the elements, return None.
