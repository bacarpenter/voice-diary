#!/usr/bin/env python3
# || ---------- app.py ---------- ||
# SHORT DESCRIPTION
# 
# Ben Carpenter and Nancy Onyimah
# April 7, 2022
# ------------- app.py -------------
import database
from entry import Entry
import crypto
import GUI
import graphics

def main():
  database.initialize_connection()
  window = GUI.open_window()

  state_did_change = True
  state = "login" # App starts at login page

  # App Loop
  while True:
    if state_did_change:
      match state:
        case "login": 
          # Login page
          drawn_elements = GUI.draw_login(window)
          state_did_change = False
        case "read": 
          # Login page
          state_did_change = False
        case "create": 
          # Login page
          state_did_change = False
        case "close":
          break
        case _:
          exit(1)

    else:
      clicked = GUI.get_click(window)

      if clicked == GUI.login_elements['login_button']:
        print("Login Button Clicked")

      # Do something with the mouse position


  database.close_connection()
  GUI.close_window(window)



if __name__ == "__main__":
  main()