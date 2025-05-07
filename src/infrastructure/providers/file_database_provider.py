import json
import os
from datetime import datetime
from typing import Dict, List, Optional
from uuid import uuid4
from ...logger_system.loggers.application_logger import ApplicationLogger
from src.models.device import Device

class FileDatabaseProvider:
    def __init__(self, logger:ApplicationLogger, db_path: str = "data/devices.json"):
        self.db_path = db_path
        self._ensure_db_exists()
        self.logger=logger
        self.logger.info(f"FileDatabaseProvider initialized. Filepath {db_path}")
   
    def _ensure_db_exists(self) -> None:
        """Create database file and parent directories if they don't exist"""
        try:
            os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
            if not os.path.exists(self.db_path):
                with open(self.db_path, "w") as f:
                    json.dump({"devices": {}}, f)
        except Exception as e:    
            self.logger.error(f"exception while creation of file database", e)
   
    def _read_db(self) -> Dict:
        """Read database file"""
        with open(self.db_path, "r") as f:
            return json.load(f)
   
    def _write_db(self, data: Dict) -> None:
        """Write to database file"""
        try:
            with open(self.db_path, "w") as f:
                json.dump(data, f, default=str)
        except Exception as e:    
            self.logger.error(f"exception while writing to file database", e)
   
    def create(self, device: Device) -> Device:
        """Create a new device entry"""
        data = self._read_db()
        device.id = str(uuid4())
        device.date_added = datetime.now()
        device.date_modified = device.date_added
        data["devices"][device.id] = device.__dict__
        self._write_db(data)
        return device
   
    def read(self, device_id: str) -> Optional[Device]:
        """Read a device by ID"""
        data = self._read_db()
        device_data = data["devices"].get(device_id)
        if not device_data:
            self.logger.info(f"no device data {device_id}")
            return None
        return Device(**device_data)
   
    def read_all(self) -> List[Device]:
        """Read all devices"""
        data = self._read_db()
        return [Device(**device_data) for device_data in data["devices"].values()]
   
    def update(self, device: Device) -> Optional[Device]:
        """Update an existing device"""
        if not device.id:
            return None
           
        data = self._read_db()
        if device.id not in data["devices"]:
            return None
           
        # Preserve original date_added
        device.date_added = data["devices"][device.id]["date_added"]
        device.date_modified = datetime.now()
       
        data["devices"][device.id] = device.__dict__
        self._write_db(data)
        return device
   
    def delete(self, device_id: str) -> bool:
        """Delete a device by ID"""
        data = self._read_db()
        if device_id not in data["devices"]:
            return False
           
        del data["devices"][device_id]
        self._write_db(data)
        return True