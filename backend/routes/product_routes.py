from flask import Blueprint
from services.products.products_service import get_products, create_products, delete_products, \
    update_products

products_routes = Blueprint("products", __name__)

# Get Mercadoria
@products_routes.route("/api/mercadorias", methods=["GET"])
def get_mercadorias():
    return get_products()

# Create Mercadoria
@products_routes.route("/api/mercadorias", methods=["POST"])
def create_mercadoria():
    return create_products()

# Delete Mercadoria
@products_routes.route("/api/mercadorias/<int:id>", methods=["DELETE"])
def delete_mercadoria(id):
    return delete_products(id)

# Update Mercadoria
@products_routes.route("/api/mercadorias/<int:id>", methods=["PATCH"])
def update_mercadoria(id):
    return update_products(id)