import sqlite3

conn = sqlite3.connect('database.db')

SCHEMA = "schema.sql"

with open(SCHEMA) as f:
    conn.executescript(f.read())

conn.commit()
conn.close()