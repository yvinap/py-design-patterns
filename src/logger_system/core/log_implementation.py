from abc import ABC, abstractmethod

class LoggerImplementation(ABC):
    @abstractmethod
    def write_info(self, message: str) -> None:
        pass
   
    @abstractmethod
    def write_warning(self, message: str) -> None:
        pass
   
    @abstractmethod
    def write_error(self, message: str, error: Exception) -> None:
        pass