from datetime import datetime
from src.models.device import Device
from ...logger_system.loggers.application_logger import ApplicationLogger
from ...logger_system.backends.console_log_implementation import ConsoleLogImplementation

class DeviceFactory:
    def __init__(self):
        console_log_impl = ConsoleLogImplementation()
        self.logger=ApplicationLogger(console_log_impl)
    
    def create_device(self,name: str, model: str, vendor: str, type: str) -> Device:
        """Create a new device instance"""
        self.logger.info(f"creating new device {name}-{model}-{vendor}-{type}")
        return Device(
            name=name,
            model=model,
            vendor=vendor,
            type=type
        )
   
    def update_device(self,device: Device, **kwargs) -> Device:
        """Update device fields"""
        self.logger.info(f"updating device {device.id}")
        for key, value in kwargs.items():
            if hasattr(device, key):
                setattr(device, key, value)
        return device