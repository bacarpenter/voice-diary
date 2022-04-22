import crypto
import database

database.initialize_connection(schema="voice_diary_test")
key = crypto.convert_passphrase_to_key("the cow jumped over the moon")

i = int(input("# "))

j = 0
while j < i:
    title = crypto.encrypt(f"Title #{i}", key)
    text = crypto.encrypt(f"This is my entry, which is of course, #{i}", key)
    database.create_entry(title, text)
    j += 1

database.close_connection()