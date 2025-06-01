from flask import Blueprint
from services.category.category_service import get_category, create_category, delete_category, \
    update_category

category_routes = Blueprint("category", __name__)

# Get Categoria
@category_routes.route("/api/categorias", methods=["GET"])
def get_categoria():
    return get_category()

# Create Categoria
@category_routes.route("/api/categorias", methods=["POST"])
def create_categoria():
    return create_category()
    
# Delete Categoria
@category_routes.route("/api/categorias/<int:id>", methods=["DELETE"])
def delete_categoria(id):
    return delete_category(id)

# Update Categoria
@category_routes.route("/api/categorias/<int:id>", methods=["PATCH"])
def update_categoria(id):
    return update_category(id)