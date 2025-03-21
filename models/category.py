class Category:
    """Represents a product category"""
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"Category: {self.name}, Description: {self.description}"
