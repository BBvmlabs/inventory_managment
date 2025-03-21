from flask import render_template
from database.db import get_db_connection

def get_all_products():
    """Retrieves all products from the database"""
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM product').fetchall()
    conn.close()
    return render_template('product.html', products=products)
