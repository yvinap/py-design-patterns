import os
from ..logger_system.loggers.application_logger import ApplicationLogger
from ..logger_system.loggers.user_change_logger import UserChangeLogLogger
from ..logger_system.backends.file_log_implementation import FileLogImplementation
from ..logger_system.backends.console_log_implementation import ConsoleLogImplementation

class ApplicationBase():
    def __init__(self):
        logging_level = os.environ.get("LOGGER_LEVEL",2)
        file_log_impl = FileLogImplementation()
        console_log_impl = ConsoleLogImplementation()
        self.app_logger=ApplicationLogger(console_log_impl, int(logging_level))
        self.user_change_logger=UserChangeLogLogger(file_log_impl,int(logging_level))
        self.app_logger.info("Application base Initialized")
        