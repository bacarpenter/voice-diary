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
  window.setBackground(graphics.color_rgb(255, 196, 252))

  passphrase = ""

  state_did_change = True
  state = "login" # App starts at login page

  # App Loop
  while True:
    if state_did_change:
      match state:
        case "login": 
          # Login page
          GUI.draw_login(window)
          state_did_change = False
        case "read": 
          # Read page
          
          GUI.draw_read(window, )
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
      print(clicked)
      if clicked == 'login_button':
        state = "read" # Once the login is completed, change the state to read mode
        state_did_change = True

      if clicked == 'create':
        state = "create"
        state_did_change = True

      if clicked == 'save':
        state == "read"
        state_did_change = True

      if clicked == "logout":
        break
     


  database.close_connection()
  GUI.close_window(window)



if __name__ == "__main__":
  main()