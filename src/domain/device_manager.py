from typing import List, Optional

from src.domain.factories.device_factory import DeviceFactory
from src.domain.repositories.device_repository import DeviceRepository
from src.models.device import Device
from ..logger_system.loggers.application_logger import ApplicationLogger
from ..logger_system.backends.console_log_implementation import ConsoleLogImplementation

class DeviceManager:
    def __init__(self, repository=None, factory=None):
        self.repository = DeviceRepository()
        self.factory = DeviceFactory()
        console_log_impl = ConsoleLogImplementation()
        self.logger=ApplicationLogger(console_log_impl)
        self.logger.info("DeviceManager initialized")
   
    def add_device(self, name: str, model: str, vendor: str, type: str) -> Device:
        """Add a new device"""
        device = self.factory.create_device(name, model, vendor, type)
        self.logger.info("adding device to repository")
        return self.repository.add(device)
   
    def get_device(self, device_id: str) -> Optional[Device]:
        """Get a device by ID"""
        return self.repository.get(device_id)
   
    def get_all_devices(self) -> List[Device]:
        """Get all devices"""
        return self.repository.get_all()
   
    def update_device(self, device_id: str, **kwargs) -> Optional[Device]:
        """Update an existing device"""
        device = self.repository.get(device_id)
        if not device:
            self.logger.info(f"device not found {device_id}")
            return None
       
        updated_device = self.factory.update_device(device, **kwargs)
        return self.repository.update(updated_device)
   
    def delete_device(self, device_id: str) -> bool:
        """Delete a device by ID"""
        self.logger.info(f"deleting devices from repository {device_id}")
        return self.repository.delete(device_id)