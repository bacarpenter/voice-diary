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
import speech_recognition as sr

def main():
  database.initialize_connection()
  print("--- Voice Diary | Ben Carpenter & Nancy Onyimah ---")

  print("Speak passphrase now:")
  passphrase = get_passphrase()
  print(f"You said: {passphrase}")
  key = crypto.convert_passphrase_to_key(passphrase)

  mode = input("Would you like to (W)rite or (R)ead an entry? ")

  if mode == "w" or mode == "W":
    title = input("Title: ")
    text = input("Body: ")

  # Encrypt the text
    title = crypto.encrypt(title, key)
    text = crypto.encrypt(text, key)

    database.create_entry(title, text)

  elif mode == "r" or mode == "R":
    print("List of all entries: ")
    entries = database.read_all_entries()
    for entry in entries:
      entry.decrypt(key)
      print(f"[{entry.id}] {entry.title} | {entry.timestamp}")

    id = input("Which entry would you like to read?")
    entry = database.read_entry(id)
    entry.decrypt(key)

    print(f"---------- {entry.title} ----------")
    print(entry.text)

  database.close_connection()



def get_passphrase() -> str:
  # https://realpython.com/python-speech-recognition/
  r = sr.Recognizer()
  mic = sr.Microphone()

  with mic as source:
    audio = r.listen(source)

  passphrase = r.recognize_google(audio)
  return passphrase
  
if __name__ == "__main__":
  main()