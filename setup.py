#!/usr/bin/env python3
# || ---------- setup.py ---------- ||
# Python script to set user up for use 
# of voice diary
# 
# Ben Carpenter and Nancy Onyimah
# April 17, 2022
# ------------- setup.py -------------
import subprocess
import os
def main():
    print("---------- Voice Diary Setup ----------")
    print("This program will walk you through setting up voice-diary")

    print("[1/4] Installing dependencies... ", end="")
    subprocess.run(["python3", "-m", "pip", "install", "-r", "requirements.txt", "-q"]) #https://stackabuse.com/executing-shell-commands-with-python/
    subprocess.run(["brew", "install", "portaudio"])
    print("done ✅")

    print("[2/4] Checking that mysql is installed... ", end="")
    if subprocess.run(["mysql", "--version"], stdout=subprocess.DEVNULL).returncode == 0:
        print("done ✅")

    else:
        print("You do not have mysql installed, it is not running, or it is not on your path.")
        exit(1)
    
    

    username = input("What is your local mysql username? (This will not be saved after execution) ")
    password = input("What is your local mysql password? (This will not be saved after execution) ")
    print("[3/4] Configuring database... ", end="")
    # Configure database
    if os.system(f"mysql -u {username} --password={password} < mysql_scripts/database_creation.sql >/dev/null 2>&1") != 0: #https://stackoverflow.com/a/33989346
        print("My SQL could not create the database. Made sure you have permissions.")
        exit(2)

    print("done ✅")

    print("[4/4] Creating voice-diary mysql user... ", end="")
    if os.system(f"mysql -u {username} --password={password} < mysql_scripts/add_user.sql >/dev/null 2>&1") != 0:
        print("My SQL could not create the user. Made sure you have permissions.")
        exit(2)
    
    

    print("done ✅")


    print("Voice diary is now ready for use! Run it with: python3 app.py")
    print("---------- Voice Diary Setup ----------")
    exit(0)

if __name__ == "__main__":
    main()