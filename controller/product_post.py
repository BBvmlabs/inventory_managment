from flask import request, redirect, url_for, flash
from database.db import get_db_connection
from models.factory import Factory

def add_product():
    """Handles adding a new product"""
    try:
        name = request.form['name']
        price = float(request.form['price'])
        category_id = int(request.form['category_id'])
        quantity = int(request.form['quantity'])
        product_id = f"SKU{category_id}{quantity}"

        product = Factory.create(
            "product",
            product_id=product_id,
            name=name,
            price=price,
            category_id=category_id,
            quantity=quantity
        )

        conn = get_db_connection()
        conn.execute(
            'INSERT INTO product (product_id, name, price, category_id, quantity) VALUES (?, ?, ?, ?, ?)',
            (product.product_id, product.name, product.price, product.category_id, product.quantity)
        )
        conn.commit()
        conn.close()

        flash('Product added successfully!', 'success')
        return redirect(url_for('index'))

    except Exception as e:
        flash(f'Error: {str(e)}', 'error')
        return redirect(url_for('index'))
