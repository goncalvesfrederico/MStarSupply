from flask import Blueprint
from services.location.location_service import get_location, create_location, delete_location, \
    update_location

location_routes = Blueprint("location", __name__)

# Get Local
@location_routes.route("/api/locais", methods=["GET"])
def get_local():
    return get_location()

# Create Local
@location_routes.route("/api/locais", methods=["POST"])
def create_local():
    return create_location()

# Delete Local
@location_routes.route("/api/locais/<int:id>", methods=["DELETE"])
def delete_local(id):
    return delete_location(id)

# Update Local
@location_routes.route("/api/locais/<int:id>", methods=["PATCH"])
def update_local(id):
    return update_location(id)
