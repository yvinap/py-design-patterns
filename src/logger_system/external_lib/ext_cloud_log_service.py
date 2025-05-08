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