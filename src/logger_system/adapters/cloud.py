from ..core.log_implementation import LoggerImplementation
from ..external_lib.ext_cloud_log_service import CloudLogService
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