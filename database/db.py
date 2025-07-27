import sqlite3

def get_db():
    db = sqlite3.connect("banco.db")
    try:
        yield db
    finally:
        db.close()