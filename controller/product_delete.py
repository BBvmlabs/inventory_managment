from flask import redirect, url_for, flash
from database.db import get_db_connection

def delete_product(product_id):
    """Deletes a product"""
    try:
        conn = get_db_connection()
        conn.execute('DELETE FROM product WHERE product_id = ?', (product_id,))
        conn.commit()
        conn.close()

        flash('Product deleted successfully!', 'success')
        return redirect(url_for('index'))

    except Exception as e:
        flash(f'Error: {str(e)}', 'error')
        return redirect(url_for('index'))
