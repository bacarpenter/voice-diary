#!/usr/bin/env python3
# || ---------- test_database.py ---------- ||
# Tests for database.py
# 
# Ben Carpenter and Nancy Onyimah
# April 24, 2022
# ------------- test_database.py -------------


import database
import mysql.connector

database.initialize_connection(schema="voice_diary_test") # Open the test schema. 
# Note: To run these tests, you will need to create an additional schema, called voice_diary_test, and grant python_user
#       permission to use it.

def clear_database():
    """Delete all entries from the database for reproducible testing"""
    cursor = database.db.cursor()
    cursor.execute("DELETE FROM `voice_diary_test`.`entries`")
    database.db.commit()
    cursor.close()

def test_initialize_connection():
    """
    Test that:
        1. initialize_connection() returns a MySQLConnection
    """

    assert type(database.db) == mysql.connector.connection_cext.CMySQLConnection

def test_create_entry():
    """
    Test that:
        1. CE returns an int of the new items id
        2. CE returns an int of different id each time
        3. The entry can be retrived with the id
    """

    clear_database() # Start with a clean database
    title = "My Title"
    text = "My secrets"
    entry_id_1 = database.create_entry(title, text)
    entry_id_2 = database.create_entry(title, text)

    assert type(entry_id_1) == int
    assert entry_id_1 != entry_id_2
    loaded = database.read_entry(entry_id_1)
    assert loaded.title == title and loaded.text == text


def test_read_entry():
    """
    Test that:
        1. Entries can by read with their id
    """

    clear_database()

    entry_id = database.create_entry("Title", "Text")

    load = database.read_entry(entry_id)

    assert load.text == "Text" and load.title == "Title"

def test_read_all_entries():
    """
    Test that:
        1. Function returns the right number of entries
    """

    clear_database()

    database.create_entry("Title 1", "Text 1")
    database.create_entry("Title 2", "Text 2")
    database.create_entry("Title 3", "Text 3")
    database.create_entry("Title 4", "Text 4")

    assert len(database.read_all_entries()) == 4

