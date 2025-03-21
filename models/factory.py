from models.products import Product
from models.category import Category

class Factory:
    """Factory for creating Product and Category instances"""

    @staticmethod
    def create(entity_type, **kwargs):
        """Factory method to create Product or Category objects"""
        if entity_type == "product":
            return Product(
                product_id=kwargs.get("product_id"),
                name=kwargs.get("name"),
                price=kwargs.get("price"),
                category_id=kwargs.get("category_id"),
                quantity=kwargs.get("quantity")
            )
        elif entity_type == "category":
            return Category(
                name=kwargs.get("name"),
                description=kwargs.get("description")
            )
        else:
            raise ValueError(f"Unknown entity type: {entity_type}")
