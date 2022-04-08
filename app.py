#!/usr/bin/env python3
# || ---------- app.py ---------- ||
# SHORT DESCRIPTION
# 
# Ben Carpenter and Nancy Onyimah
# April 7, 2022
# ------------- app.py -------------


def main():
  decision = input("Welcome! Do you want to write an entries or read an existing one?")
  
  if decision == "w" or "W":
    create_entry()
  if decision == "r" or "R":
    read_entry()

  title = input ("What is the title of your entry?")

  text = input ("What do you want to write in your entry?")
  pass

def create_entry(text, title):
  print(f"Entry created of title {title} and content {text}")

def read_all_entries():
  pass

def read_entry(id):
  pass


if __name__ == "__main__":
  main()