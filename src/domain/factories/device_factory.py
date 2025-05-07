from datetime import datetime
from src.models.device import Device

class DeviceFactory:
    @staticmethod
    def create_device(name: str, model: str, vendor: str, type: str) -> Device:
        """Create a new device instance"""
        print(f"creating new device {name}-{model}-{vendor}-{type}")
        return Device(
            name=name,
            model=model,
            vendor=vendor,
            type=type
        )
   
    @staticmethod
    def update_device(device: Device, **kwargs) -> Device:
        """Update device fields"""
        print(f"updating device {device.id}")
        for key, value in kwargs.items():
            if hasattr(device, key):
                setattr(device, key, value)
        return device