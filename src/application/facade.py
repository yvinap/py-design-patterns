import os
from typing import Dict, List, Optional

from src.domain.device_manager import DeviceManager
from ..logger_system.loggers.application_logger import ApplicationLogger
from ..logger_system.backends.file_log_implementation import FileLogImplementation
from ..logger_system.backends.console_log_implementation import ConsoleLogImplementation

class ApplicationFacade:
    def __init__(self):
        log_impl = None
        logger_type = os.environ.get("LOGGER_TYPE","CONSOLE")
        if logger_type.__eq__("FILE"):
            log_impl = FileLogImplementation()
        else:
            log_impl = ConsoleLogImplementation()
        logger=ApplicationLogger(log_impl)
        self.logger=logger
        self.logger.info("Application Facade Initialized")
        self.device_manager = DeviceManager(self.logger)
        
    def add_device(self, name: str, model: str, vendor: str, type: str) -> Dict:
        """Add a new device"""
        try:
            device = self.device_manager.add_device(name, model, vendor, type)
            return {"success": True, "data": device.__dict__}
        except Exception as e:
            self.logger.error(f"Exception in add_device. {name}-{model}-{vendor}-{type}", e)
            return {"success": False, "error": str(e)}
   
    def get_device(self, device_id: str) -> Dict:
        """Get a device by ID"""
        try:
            device = self.device_manager.get_device(device_id)
            if not device:
                return {"success": False, "error": "Device not found"}
            return {"success": True, "data": device.__dict__}
        except Exception as e:
            self.logger.error(f"Exception in get_device.", e)
            return {"success": False, "error": str(e)}
   
    def get_all_devices(self) -> Dict:
        """Get all devices"""
        try:
            self.logger.warning(f"get_all_devices. test warning")
            devices = self.device_manager.get_all_devices()
            return {"success": True, "data": [device.__dict__ for device in devices]}
        except Exception as e:
            self.logger.error(f"Exception in get_all_devices. {str(e)}")
            return {"success": False, "error": str(e)}
   
    def update_device(self, device_id: str, **kwargs) -> Dict:
        """Update an existing device"""
        try:
            device = self.device_manager.update_device(device_id, **kwargs)
            if not device:
                return {"success": False, "error": "Device not found"}
            return {"success": True, "data": device.__dict__}
        except Exception as e:
            self.logger.error(f"Exception in update_device {device_id}", e)
            return {"success": False, "error": str(e)}
   
    def delete_device(self, device_id: str) -> Dict:
        """Delete a device by ID"""
        try:
            self.logger.info(f"deleting device {device_id}")
            success = self.device_manager.delete_device(device_id)
            if not success:
                return {"success": False, "error": "Device not found"}
            return {"success": True}
        except Exception as e:
            self.logger.error(f"Exception in delete_device {device_id}", e)
            return {"success": False, "error": str(e)}