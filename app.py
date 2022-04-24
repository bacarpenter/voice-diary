#!/usr/bin/env python3
# || ---------- app.py ---------- ||
# SHORT DESCRIPTION
# 
# Ben Carpenter and Nancy Onyimah
# April 7, 2022
# ------------- app.py -------------
from crypt import crypt
from email.quoprimime import body_check
from time import sleep
import database
from entry import Entry
import crypto
import GUI
import graphics
import speech_recognition as sr
import spech_rec_helpers as sr_helpers
from playsound import playsound 

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
          entries.sort(key = lambda x: x.timestamp)
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

      match clicked:
        case 'login_button':

          recognizer = sr.Recognizer()
          microphone = sr.Microphone()

          # Listen for speech
          GUI.update_login_notification("Wait 1 second and speak...")
          spoken_phrase = sr_helpers.recognize_speech_from_mic(recognizer, microphone)

          if spoken_phrase['success'] == False:
            GUI.update_login_notification("Sorry, something went wrong. Try again")
          elif spoken_phrase['transcription'] == None:
            GUI.update_login_notification("We didn't hear anything")
          else:
            passphrase = crypto.convert_passphrase_to_key(spoken_phrase['transcription'])

            # Check if passphrase is correct by seeing if it decrypts an entry. If there are no entries, ignore this check
            all_entries = database.read_all_entries()
            if len(all_entries) != 0:
              all_entries[0].decrypt(passphrase)
              if  all_entries[0].text == None:
                GUI.update_login_notification(f"Incorrect passphrase. We heard: {spoken_phrase['transcription']}")
              else:
                state = "read" # Once the login is completed, change the state to read mode
                state_did_change = True
            else:
              state = "read" # Once the login is completed, change the state to read mode
              state_did_change = True

        case 'create':
          GUI.draw_create(window)
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
          title = GUI.create_elements['title_entry'].getText()
          title = crypto.encrypt(title, passphrase)
          body = GUI.create_elements['create_body_entry'].getText()
          body = crypto.encrypt(body, passphrase)

          database.create_entry(title, body)
          
          database.close_connection()
          database.initialize_connection()

          state = "read"
          state_did_change = True

        case 'back_to_read':
          state = "read"
          state_did_change = True

        case "logout":
          break

      if type(clicked) == int:
        entry = database.read_entry(clicked)
        entry.decrypt(passphrase)
        GUI.draw_read_entry(window, entry.title, entry.text)
     


  database.close_connection()
  GUI.close_window(window)



if __name__ == "__main__":
  main()