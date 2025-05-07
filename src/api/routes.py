from flask import Blueprint, jsonify, request

from src.api.validators import validate_device_data
from src.application.facade import ApplicationFacade
from ..logger_system.loggers.application_logger import ApplicationLogger

api = Blueprint("api", __name__)

facade = ApplicationFacade()

@api.route("/devices", methods=["POST"])
def add_device():
    """Add a new device"""
    data = request.json
   
    # Validate request data
    errors = validate_device_data(data)
    if errors:
        return jsonify({"success": False, "errors": errors}), 400
   
    result = facade.add_device(
        name=data["name"],
        model=data["model"],
        vendor=data["vendor"],
        type=data["type"]
    )
   
    if result["success"]:
        return jsonify(result), 201
    return jsonify(result), 500

@api.route("/devices/<device_id>", methods=["GET"])
def get_device(device_id):
    """Get a device by ID"""
    result = facade.get_device(device_id)
   
    if result["success"]:
        return jsonify(result), 200
    return jsonify(result), 404

@api.route("/devices", methods=["GET"])
def get_all_devices():
    """Get all devices"""
    result = facade.get_all_devices()
   
    if result["success"]:
        return jsonify(result), 200
    return jsonify(result), 500

@api.route("/devices/<device_id>", methods=["PUT"])
def update_device(device_id):
    """Update an existing device"""
    data = request.json
   
    # Allow partial updates
    update_fields = {}
    for field in ["name", "model", "vendor", "type"]:
        if field in data:
            update_fields[field] = data[field]
   
    result = facade.update_device(device_id, **update_fields)
   
    if result["success"]:
        return jsonify(result), 200
    return jsonify(result), 404

@api.route("/devices/<device_id>", methods=["DELETE"])
def delete_device(device_id):
    """Delete a device by ID"""
    result = facade.delete_device(device_id)
   
    if result["success"]:
        return jsonify(result), 200
    return jsonify(result), 404