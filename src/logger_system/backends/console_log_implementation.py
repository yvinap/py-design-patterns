import traceback
from ..core.log_implementation import LoggerImplementation

class ConsoleLogImplementation(LoggerImplementation):
    def write_info(self, message: str) -> None:
        print(f"[INFO] {message}")
   
    def write_warning(self, message: str) -> None:
        print(f"[WARNING] {message}")
   
    def write_error(self, message: str, error: Exception) -> None:
        print(f"[ERROR] {message}")
        traceback.print_exception(type(error), error, error.__traceback__)