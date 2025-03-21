from flask import request, redirect, url_for, flash
from database.db import get_db_connection

def update_category(category_id):
    """Updates an existing category"""
    try:
        name = request.form['name']
        description = request.form['description']

        conn = get_db_connection()
        conn.execute(
            'UPDATE category SET name = ?, description = ? WHERE id = ?',
            (name, description, category_id)
        )
        conn.commit()
        conn.close()

        flash('Category updated successfully!', 'success')
        return redirect(url_for('index'))

    except Exception as e:
        flash(f'Error: {str(e)}', 'error')
        return redirect(url_for('index'))
