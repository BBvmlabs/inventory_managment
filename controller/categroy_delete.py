from flask import redirect, url_for, flash
from database.db import get_db_connection

def delete_category(category_id):
    """Deletes a category"""
    try:
        conn = get_db_connection()
        conn.execute('DELETE FROM category WHERE id = ?', (category_id,))
        conn.commit()
        conn.close()

        flash('Category deleted successfully!', 'success')
        return redirect(url_for('index'))

    except Exception as e:
        flash(f'Error: {str(e)}', 'error')
        return redirect(url_for('index'))
