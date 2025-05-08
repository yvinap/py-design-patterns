from datetime import datetime
from src.models.device import Device
from ...application.app_base import ApplicationBase

class DeviceFactory:
    def __init__(self,a_base:ApplicationBase):
        self.a_base = a_base
    
    def create_device(self,name: str, model: str, vendor: str, type: str) -> Device:
        """Create a new device instance"""
        self.a_base.app_logger.info(f"creating new device {name}-{model}-{vendor}-{type}")
        return Device(
            name=name,
            model=model,
            vendor=vendor,
            type=type
        )
   
    def update_device(self,device: Device, **kwargs) -> Device:
        """Update device fields"""
        self.a_base.app_logger.info(f"updating device {device.id}")
        for key, value in kwargs.items():
            if hasattr(device, key):
                setattr(device, key, value)
        return device