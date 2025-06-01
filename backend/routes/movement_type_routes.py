from flask import Blueprint
from services.movement_type.movement_service import get_movement_type, create_movement_type, \
    delete_movement_type, update_movement_type

movement_type_routes = Blueprint("movemente_type", __name__)

# Get Fabricante
@movement_type_routes.route("/api/tipomovimentacao", methods=["GET"])
def get_tipo_movimentacao():
    return get_movement_type()

# Create Fabricante
@movement_type_routes.route("/api/tipomovimentacao", methods=["POST"])
def create_tipo_movimentacao():
    return create_movement_type()

# Delete Fabricante
@movement_type_routes.route("/api/tipomovimentacao/<int:id>", methods=["DELETE"])
def delete_tipo_movimentacao(id):
    return delete_movement_type(id)

# Update Fabricante
@movement_type_routes.route("/api/tipomovimentacao/<int:id>", methods=["PATCH"])
def update_tipo_movimentacao(id):
    return update_movement_type(id)