from flask import Flask, render_template, request, redirect, url_for, flash
from database.db import get_db_connection, init_db
from controller.product_post import add_product
from controller.product_get import get_all_products
from controller.product_update import update_product
from controller.product_delete import delete_product
from controller.categroy_post import add_category
from controller.categroy_get import get_all_categories
from controller.categroy_update import update_category
from controller.categroy_delete import delete_category

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # For flash messages

# Initialize the database
init_db()


### --- ROUTES ---

# Home Route
@app.route('/')
def index():
    """Displays the home page with product and category management links"""
    conn = get_db_connection()
    
    # Fetch products and categories for display
    products = conn.execute('SELECT * FROM product').fetchall()
    categories = conn.execute('SELECT * FROM category').fetchall()
    
    conn.close()
    return render_template('index.html', products=products, categories=categories)


### --- PRODUCT ROUTES ---

# Route to display products
@app.route('/products')
def products():
    """Displays the product management page"""
    products = get_all_products()
    categories = get_all_categories()
    return render_template('product.html', products=products, categories=categories)


# Route to add a new product
@app.route('/add_product', methods=['POST'])
def add_product_route():
    """Handles adding a new product"""
    return add_product()


# Route to update product details
@app.route('/update_product/<string:product_id>', methods=['POST'])
def update_product_route(product_id):
    """Handles updating a product by ID"""
    return update_product(product_id)


# Route to delete a product
@app.route('/delete_product/<string:product_id>', methods=['POST'])
def delete_product_route(product_id):
    """Handles deleting a product by ID"""
    return delete_product(product_id)


### --- CATEGORY ROUTES ---

# Route to display categories
@app.route('/categories')
def categories():
    """Displays the category management page"""
    categories = get_all_categories()
    return render_template('category.html', categories=categories)


# Route to add a new category
@app.route('/add_category', methods=['POST'])
def add_category_route():
    """Handles adding a new category"""
    return add_category()


# Route to update category details
@app.route('/update_category/<int:category_id>', methods=['POST'])
def update_category_route(category_id):
    """Handles updating a category by ID"""
    return update_category(category_id)


# Route to delete a category
@app.route('/delete_category/<int:category_id>', methods=['POST'])
def delete_category_route(category_id):
    """Handles deleting a category by ID"""
    return delete_category(category_id)


### --- RUN APP ---
if __name__ == '__main__':
    app.run(debug=True)
