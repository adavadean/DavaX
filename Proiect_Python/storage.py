import sqlite3
from model import Result

def init_db():
    conn = sqlite3.connect("math.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS operations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            operation TEXT,
            x INTEGER,
            y INTEGER,
            result INTEGER
        )
    """)
    conn.commit()
    conn.close()

def save_result(res: Result):
    conn = sqlite3.connect("math.db")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO operations (operation, x, y, result) VALUES (?, ?, ?, ?)",
        (res.operation, res.x, res.y, res.result)
    )
    conn.commit()
    conn.close()
