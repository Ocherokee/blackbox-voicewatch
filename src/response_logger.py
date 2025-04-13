import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'session_logs.db')

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            input_phrase TEXT,
            response TEXT,
            tag TEXT,
            notes TEXT,
            audio_file TEXT
        )
    ''')
    conn.commit()
    conn.close()

def log_response(input_phrase, response, tag, notes, audio_file):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    timestamp = datetime.now().isoformat()
    cursor.execute('''
        INSERT INTO logs (timestamp, input_phrase, response, tag, notes, audio_file)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (timestamp, input_phrase, response, tag, notes, audio_file))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized and ready for logging.")

