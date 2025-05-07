import json
import os
from datetime import datetime
from typing import Dict, List, Optional
from ..core.log_implementation import LoggerImplementation

class FileLogImplementation(LoggerImplementation):
    def __init__(self, file_path: str= "logs/logs.json"):
        self.file_path = file_path
        # In a real implementation, we'd open the file here
        print(f"Initializing file logger at {file_path}")
        self._ensure_file_log_exists()
   
    def write_info(self, message: str) -> None:
        # Write to file: "[INFO] message"
        log_message = (f"Writing to file: [INFO] {message}")
        self._write_log_file(log_message)
   
    def write_warning(self, message: str) -> None:
        # Write to file: "[WARNING] {message}"
        log_message = (f"Writing to file: [WARNING] {message}")
        self._write_log_file(log_message)
   
    def write_error(self, message: str, error: Exception) -> None:
        # Write to file: "[ERROR] message" and stack trace
        log_message = (f"Writing to file: [ERROR] {message}") + (f"Writing exception: {str(error)}")
        self._write_log_file(log_message)
    
    def _ensure_file_log_exists(self) -> None:
        """Create log file and parent directories if they don't exist"""
        try:
            os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
            if not os.path.exists(self.file_path):
                with open(self.file_path, "w") as f:
                    json.dump({"logs": {}}, f)
        except Exception as e:    
            print(f"exception while creation of log file", e)
   
    def _read_log_file(self) -> Dict:
        """Read log file"""
        with open(self.file_path, "r") as f:
            return json.load(f)
   
    def _write_log_file(self, log_message: str) -> None:
        """Write to log file"""
        try:
            data = self._read_log_file()
            data["logs"][datetime.strftime(datetime.now(),"%d/%m/%Y, %H:%M:%S.%f")]=log_message
            with open(self.file_path, "w") as f:
                json.dump(data, f, default=str)
        except Exception as e:    
            print(f"exception while writing to file log", e)