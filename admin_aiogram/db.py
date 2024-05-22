import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Define the users table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        userid INTEGER NOT NULL UNIQUE,
        fullname TEXT NOT NULL
    )
''')
conn.commit()


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_user(self, userid, fullname):
        with self.connection:
            return self.cursor.execute("INSERT INTO users (userid,fullname) VALUES (?,?)", (userid, fullname))

    def all_userid(self):
        with self.connection:
            return self.cursor.execute("SELECT userid FROM users").fetchall()