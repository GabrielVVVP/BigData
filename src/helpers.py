import sqlite3
import os

def get_db_connection():
    # Configuração do banco de dados
    db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), './database/data.db'))
    # Ensure the 'data' directory exists
    data_dir = os.path.dirname(db_path)
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Create the database file if it doesn't exist
    if not os.path.exists(db_path):
        with open(db_path, 'w'):
            pass

    # Connect to the database
    conn = sqlite3.connect(db_path, check_same_thread=False)
    return conn

def initialize_database():
    with get_db_connection() as conn:
        c = conn.cursor()

        c.execute('''CREATE TABLE IF NOT EXISTS participants (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            idade TEXT,
            interesse TEXT
        )''')

        conn.commit()
        return
    
def create_participant(name, age, interest):
    """Add a new participant."""
    with get_db_connection() as conn:
        try:
            c = conn.cursor()
            c.execute("INSERT INTO participants (nome, idade, interesse) VALUES (?, ?, ?)", (name, age, interest))
            conn.commit()
            return True, "Participante criado corretamente!"
        except sqlite3.IntegrityError as e:
            return False, f"Error: {str(e)}"

def get_participants():
    """Fetch all participants."""
    with get_db_connection() as conn:
        try:
            c = conn.cursor()
            c.execute("SELECT * FROM participants")
            return True, c.fetchall()
        except sqlite3.IntegrityError as e:
            return False, f"Error: {str(e)}"             