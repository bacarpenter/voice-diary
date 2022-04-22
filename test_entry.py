from datetime import datetime
from entry import Entry
import crypto

def test_construction():
    """
    Test that:
        1. Class construction works
        2. Fields are accessible
    """

    dt = datetime.now()
    e = Entry(0, "Title", "Text", dt)
    assert type(e) == Entry
    assert e.title == "Title" and e.text == "Text" and e.timestamp == dt

def test_decrypt():
    """
    Test that:
        1. The decypts method decrypts all fields properly
    """
    key = crypto.convert_passphrase_to_key("the cow jumped over the moon")

    enc_title = crypto.encrypt("Title", key)
    enc_text = crypto.encrypt("Text", key)

    e = Entry(0, enc_title, enc_text, datetime.now())

    e.decrypt(key)

    assert e.title == "Title" and e.text == "Text"



