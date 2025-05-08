from typing import List, Optional

from src.infrastructure.database.database_service import DatabaseService
from src.models.device import Device
from ...application.app_base import ApplicationBase

class DeviceRepository:
    def __init__(self, a_base:ApplicationBase):
        self.a_base = a_base
        self.db_service = DatabaseService(self.a_base)
   
    def add(self, device: Device) -> Device:
        """Add a new device"""
        return self.db_service.create_device(device)
   
    def get(self, device_id: str) -> Optional[Device]:
        """Get a device by ID"""
        return self.db_service.get_device(device_id)
   
    def get_all(self) -> List[Device]:
        """Get all devices"""
        return self.db_service.get_all_devices()
   
    def update(self, device: Device) -> Optional[Device]:
        """Update an existing device"""
        return self.db_service.update_device(device)
   
    def delete(self, device_id: str) -> bool:
        """Delete a device by ID"""
        return self.db_service.delete_device(device_id)