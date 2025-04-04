import sqlite3

def create_table():
    conn = sqlite3.connect("library.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                author TEXT,
                year INTEGER
            )""")
    conn.commit()
    conn.close()

def add_book(title, author, year):
    conn = sqlite3.connect("library.db")
    c = conn.cursor()
    c.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", (title, author, year))
    conn.commit()
    conn.close()

def view_books():
    conn = sqlite3.connect("library.db")
    c = conn.cursor()
    c.execute("SELECT * FROM books")
    books = c.fetchall()
    conn.close()
    return books
