from typing import List, Optional

from src.domain.factories.device_factory import DeviceFactory
from src.domain.repositories.device_repository import DeviceRepository
from src.models.device import Device
from ..application.app_base import ApplicationBase

class DeviceManager:
    def __init__(self,a_base:ApplicationBase):
        self.a_base = a_base
        self.a_base.app_logger=a_base.app_logger
        self.repository = DeviceRepository(self.a_base)
        self.factory = DeviceFactory(self.a_base)
        self.a_base.app_logger.info("DeviceManager initialized")
   
    def add_device(self, name: str, model: str, vendor: str, type: str) -> Device:
        """Add a new device"""
        device = self.factory.create_device(name, model, vendor, type)
        self.a_base.app_logger.info("adding device to repository")
        self.a_base.user_change_logger.info(f"{device.name} Added")
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
            self.a_base.app_logger.info(f"device not found {device_id}")
            return None
       
        updated_device = self.factory.update_device(device, **kwargs)
        self.a_base.user_change_logger.info(f"{device.name} Updated")
        return self.repository.update(updated_device)
   
    def delete_device(self, device_id: str) -> bool:
        """Delete a device by ID"""
        self.a_base.app_logger.info(f"deleting devices from repository {device_id}")
        self.a_base.user_change_logger.delete_record_log_audit("Device",device_id)
        return self.repository.delete(device_id)