from flask import request, redirect, url_for, flash
from database.db import get_db_connection
from models.factory import Factory

def add_category():
    """Handles adding a new category"""
    try:
        name = request.form['name']
        description = request.form['description']

        category = Factory.create(
            "category",
            name=name,
            description=description
        )

        conn = get_db_connection()
        conn.execute(
            'INSERT INTO category (name, description) VALUES (?, ?)',
            (category.name, category.description)
        )
        conn.commit()
        conn.close()

        flash('Category added successfully!', 'success')
        return redirect(url_for('index'))

    except Exception as e:
        flash(f'Error: {str(e)}', 'error')
        return redirect(url_for('index'))
