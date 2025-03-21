from flask import request, redirect, url_for, flash
from models.db import get_db_connection

def update_product(product_id):
    """Updates an existing product"""
    try:
        name = request.form['name']
        price = float(request.form['price'])
        category_id = int(request.form['category_id'])
        quantity = int(request.form['quantity'])

        conn = get_db_connection()
        conn.execute(
            'UPDATE product SET name = ?, price = ?, category_id = ?, quantity = ? WHERE product_id = ?',
            (name, price, category_id, quantity, product_id)
        )
        conn.commit()
        conn.close()

        flash('Product updated successfully!', 'success')
        return redirect(url_for('index'))

    except Exception as e:
        flash(f'Error: {str(e)}', 'error')
        return redirect(url_for('index'))
