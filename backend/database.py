import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect('summarize.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS summaries(
            id INTEGER PRIMARY KEY,
            filename TEXT,
            transcribe TEXT,
            summary TEXT,
            actions TEXT,
            uploaded_at TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_summary(filename, transcribe, summary, actions):
    conn = sqlite3.connect('summarize.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO summaries (filename, transcribe, summary, actions, uploaded_at)
        VALUES (?,?,?,?,?)
    ''',(filename, transcribe, summary, "/n".join(actions), datetime.now()))

    conn.commit()
    conn.close()