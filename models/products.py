class Product:
    """Represents a product"""
    def __init__(self, product_id, name, price, category_id, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category_id = category_id
        self.quantity = quantity

    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}, Stock: {self.quantity}"
