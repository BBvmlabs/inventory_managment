from flask import render_template
from models.db import get_db_connection

def get_all_categories():
    """Retrieves all categories from the database"""
    conn = get_db_connection()
    categories = conn.execute('SELECT * FROM category').fetchall()
    conn.close()
    return render_template('category.html', categories=categories)
