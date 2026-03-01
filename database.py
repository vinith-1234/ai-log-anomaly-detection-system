import sqlite3

conn = sqlite3.connect("logs.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT,
    anomaly_score REAL,
    risk TEXT
)
""")

conn.commit()

def insert_result(filename, score, risk):
    cursor.execute("INSERT INTO results (filename, anomaly_score, risk) VALUES (?, ?, ?)",
                   (filename, score, risk))
    conn.commit()