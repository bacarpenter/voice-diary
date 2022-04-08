import database

database.initialize_connection()
print(database.read_entry(1))