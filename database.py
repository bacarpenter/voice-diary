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
import datetime
from entry import Entry

db = None

def initialize_connection(schema="voice_diary"):
    global db
    """
    Start the Database connection
    """

    # Code here based on dev example https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html
    try:
        db = mysql.connector.connect(user='python_user',
                                    password='Python!',
                                    database=schema)
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
    db.close()


def create_entry(entry: Entry) -> int:
    """
    Create an entry in the database and return an int of it's ID
    """
    return create_entry(entry.title, entry.text)

def create_entry(title: str, text: str)-> int:
    """
    Create an entry in the database and return an int of it's ID
    """
    # Code here based on dev example https://dev.mysql.com/doc/connector-python/en/https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-transaction.html
    cursor = db.cursor()

    add_entry = ("INSERT INTO entries "
                "(title, text, timestamp) "
                "VALUES (%s, %s, %s)")

    entry_data = (title, text, datetime.datetime.now())

    cursor.execute(add_entry, entry_data)
    entry_id = cursor.lastrowid

    db.commit()

    cursor.close()
    return entry_id

def read_all_entries():
    """
    Return all journal entries in the database
    """

    # Code here based on https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-select.html
    cursor = db.cursor()

    query = "SELECT * FROM entries"

    cursor.execute(query)

    entries = []
    for entry in cursor:
        entries.append(Entry(entry[0], entry[1], entry[2], entry[3]))

    cursor.close()
    return entries

def read_entry(id: int):
    """
    Return the entry with given id
    """
    # Code here based on https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-select.html
    cursor = db.cursor()
    query = "SELECT * FROM entries WHERE id = %s"
    cursor.execute(query, [id])

    entries = []
    for entry in cursor:
        entries.append(entry)

    entry = entries[0]
    return Entry(entry[0], entry[1], entry[2], entry[3])