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

  page_start = 1
  page_end = 7

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
          entries = database.read_all_entries()
          for e in entries:
            e.decrypt(passphrase)
          
          GUI.draw_read(window, entries, page_start, page_end)
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

      match clicked:
        case 'login_button':
          passphrase = crypto.convert_passphrase_to_key("the cow jumped over the moon")
          state = "read" # Once the login is completed, change the state to read mode
          state_did_change = True

        case 'create':
          state = "create"
          state_did_change = True

        case 'page_up':
          page_start += 8
          page_end += 8
          state_did_change = True

        case 'page_down':
          page_start -= 8
          page_end -= 8
          state_did_change = True
          

        case 'save':
          state = "read"
          state_did_change = True

        case "logout":
          break
     


  database.close_connection()
  GUI.close_window(window)



if __name__ == "__main__":
  main()