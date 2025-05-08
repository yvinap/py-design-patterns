from abc import ABC, abstractmethod
from .log_implementation import LoggerImplementation

class LoggerAbstraction(ABC):
    def __init__(self, implementation: LoggerImplementation, logging_level="ERROR"):
        self.implementation = implementation
        self.logging_level=logging_level
   
    @abstractmethod
    def info(self, message: str) -> None:
        pass
   
    @abstractmethod
    def warning(self, message: str) -> None:
        pass
   
    @abstractmethod
    def error(self, message: str, e: Exception) -> None:
        pass