from typing import List, Optional

from src.infrastructure.providers.file_database_provider import FileDatabaseProvider
from src.models.device import Device
from ...application.app_base import ApplicationBase
class DatabaseService:
    def __init__(self, a_base:ApplicationBase):
        self.a_base=a_base
        self.provider = FileDatabaseProvider(a_base)
        self.a_base.app_logger.info("DatabaseService initialized")
   
    def create_device(self, device: Device) -> Device:
        """Create a new device"""
        return self.provider.create(device)
   
    def get_device(self, device_id: str) -> Optional[Device]:
        """Get a device by ID"""
        return self.provider.read(device_id)
   
    def get_all_devices(self) -> List[Device]:
        """Get all devices"""
        return self.provider.read_all()
   
    def update_device(self, device: Device) -> Optional[Device]:
        """Update an existing device"""
        return self.provider.update(device)
   
    def delete_device(self, device_id: str) -> bool:
        """Delete a device by ID"""
        return self.provider.delete(device_id)