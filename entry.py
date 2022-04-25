#!/usr/bin/env python3
# || ---------- entry.py ---------- ||
# A simple class to keep parts of each
# diary entry organized
# 
# Ben Carpenter and Nancy Onyimah
# April 24, 2022
# ------------- entry.py -------------

import crypto

class Entry:
    def __init__(self, id, title, text, timestamp):
        self.id = id
        self.title = title
        self.text = text
        self.timestamp = timestamp

    def decrypt(self, key: str) -> None:
        """
        Decrypt the title and the text of an entry.
        """
        self.title = crypto.decrypt(self.title, key)
        self.text = crypto.decrypt(self.text, key)