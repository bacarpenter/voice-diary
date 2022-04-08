#!/usr/bin/env python3
# || ---------- database.py ---------- ||
# Database functions
# 
# Ben Carpenter
# April 7, 2022
# ------------- database.py -------------

# Connection initialization 
import mysql.connector
from mysql.connector import errorcode

global db

def initialize_connection():
    """
    Start the Database connection
    """
    try:
        db = mysql.connector.connect(user='python_user',
                                    password='Python!',
                                    database='voice_diary')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

def close_connection():
    """
    Close the database connection
    """
    cnx.close()


def create_entry(text, title)-> int:
    """
    Create an entry in the database and return an int of it's ID
    """
    pass

def read_all_entries():
    """
    Return all journal entries in the database
    """
    pass

def read_entry(id):
    """
    Return the entry with given id
    """
    pass