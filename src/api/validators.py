from typing import Dict, Optional, Union

def validate_device_data(data: Dict) -> Union[Dict[str, str], None]:
    """Validate device data for creation and update operations"""
    errors = {}
   
    # Required fields for device creation
    required_fields = ["name", "model", "vendor", "type"]
   
    for field in required_fields:
        if field not in data:
            errors[field] = f"{field} is required"
        elif not isinstance(data[field], str):
            errors[field] = f"{field} must be a string"
        elif not data[field].strip():
            errors[field] = f"{field} cannot be empty"
   
    return errors if errors else None