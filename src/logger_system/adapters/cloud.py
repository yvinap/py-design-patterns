from ..core.log_implementation import LoggerImplementation

# External service we can't modify (Incompatible interface)
class CloudLogService:
    def log(self, level: str, source: str, message: str) -> None:
        print(f"CLOUD LOG: [{level}][{source}] {message}")
   
    def log_with_exception(self, level: str, source: str, message: str, exception: Exception) -> None:
        print(f"CLOUD LOG: [{level}][{source}] {message}")
        print(f"Exception: {exception}")
   
    # Cloud-specific methods
    def set_api_key(self, key: str) -> None:
        print(f"API Key configured: {key}")
   
    def flush_logs(self) -> None:
        print("Flushing logs to cloud storage")

# Adapter
class CloudLogAdapter(LoggerImplementation):
    def __init__(self, api_key: str, source_system: str):
        self.cloud_service = CloudLogService()
        self.source_system = source_system
        self.cloud_service.set_api_key(api_key)
        print("Cloud Watch Log Adapter initalized")
   
    def write_info(self, message: str) -> None:
        self.cloud_service.log("INFO", self.source_system, message)
   
    def write_warning(self, message: str) -> None:
        self.cloud_service.log("WARNING", self.source_system, message)
   
    def write_error(self, message: str, error: Exception) -> None:
        self.cloud_service.log_with_exception("ERROR", self.source_system, message, error)
   
    # Additional method to expose cloud-specific functionality
    def flush(self) -> None:
        self.cloud_service.flush_logs()