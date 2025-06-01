from flask import Blueprint
from services.manufacturer.manufacturer_service import get_manufacturer, \
    create_manufacturer, delete_manufacturer, update_manufacturer

manufacturer_routes = Blueprint("manufacturer", __name__)

# Get Fabricante
@manufacturer_routes.route("/api/fabricantes", methods=["GET"])
def get_fabricante():
    return get_manufacturer()

# Create Fabricante
@manufacturer_routes.route("/api/fabricantes", methods=["POST"])
def create_fabricante():
    return create_manufacturer()

# Delete Fabricante
@manufacturer_routes.route("/api/fabricantes/<int:id>", methods=["DELETE"])
def delete_fabricante(id):
    return delete_manufacturer(id)

# Update Fabricante
@manufacturer_routes.route("/api/fabricantes/<int:id>", methods=["PATCH"])
def update_fabricante(id):
    return update_manufacturer(id)