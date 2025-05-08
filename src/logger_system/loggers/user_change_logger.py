from ..core.logger_abstraction import LoggerAbstraction

class UserChangeLogLogger(LoggerAbstraction):
    def info(self, message: str) -> None:
        self.implementation.write_info(f"User Change Log: {message}")
   
    def warning(self, message: str) -> None:
        self.implementation.write_warning(f"User Change Log: {message}")
   
    def error(self, message: str, e: Exception) -> None:
        self.implementation.write_error(f"User Change Log: {message}", e)
    
    def delete_record_log_audit(self, record_info: str, record_id:str) -> None:
        self.implementation.write_warning(f"*****Record Delete Audit Log: **** {record_info}-{record_id} ")