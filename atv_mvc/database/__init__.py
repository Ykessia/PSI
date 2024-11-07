import sqlite3
import os

DATABASE = 'database/database.db'
def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn