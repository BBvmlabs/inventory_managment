import sqlite3

def get_db_connection():
    """Establishes a database connection and returns the connection object"""
    conn = sqlite3.connect("instance/inventory.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initializes the database schema"""
    with get_db_connection() as conn:
        cursor = conn.cursor()

        # Create category table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS category (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT
        )
        ''')

        # Create product table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS product (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id TEXT NOT NULL UNIQUE,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            category_id INTEGER,
            quantity INTEGER NOT NULL,
            FOREIGN KEY(category_id) REFERENCES category(id)
        )
        ''')
        conn.commit()
