from ..core.logger_abstraction import LoggerAbstraction

class ApplicationLogger(LoggerAbstraction):
    def info(self, message: str) -> None:
        if self.logging_level>2:
            self.implementation.write_info(f"APP: {message}")
   
    def warning(self, message: str) -> None:
        if self.logging_level>1:
            self.implementation.write_warning(f"APP: {message}")
   
    def error(self, message: str, e: Exception) -> None:
        self.implementation.write_error(f"APP: {message}", e)
        