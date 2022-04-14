from crypt import crypt
import crypto

class Entry:
    def __init__(self, id, title, text, timestamp):
        self.id = id
        self.title = title
        self.text = text
        self.timestamp = timestamp

    def decrypt(self, key):
        self.title = crypto.decrypt(self.title, key)
        self.text = crypto.decrypt(self.text, key)