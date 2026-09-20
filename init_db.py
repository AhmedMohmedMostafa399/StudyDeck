import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS decks (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cards (
            id INTEGER PRIMARY KEY,
            deck_id INTEGER NOT NULL,
            front TEXT NOT NULL,
            back TEXT NOT NULL,
            interval_days INTEGER DEFAULT 1,
            next_review TEXT DEFAULT CURRENT_DATE,
            FOREIGN KEY (deck_id) REFERENCES decks (id)
        )
    ''')
    conn.commit()
    conn.close()
if __name__ == '__main__':
    init_db()