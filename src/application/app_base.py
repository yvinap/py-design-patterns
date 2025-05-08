import os
from ..logger_system.loggers.application_logger import ApplicationLogger
from ..logger_system.loggers.user_change_logger import UserChangeLogLogger
from ..logger_system.backends.file_log_implementation import FileLogImplementation
from ..logger_system.backends.console_log_implementation import ConsoleLogImplementation
from ..logger_system.adapters.cloud import CloudLogAdapter
class ApplicationBase():
    def __init__(self):
        logging_level = os.environ.get("LOGGER_LEVEL",2)
        api_key = os.environ.get("CLOUD_API_KEY","C_API_KEY")
        cloud_watch_source = os.environ.get("CLOUD_WATCH_SOURCE","C_SOURCE")
        cloud_log_impl = CloudLogAdapter(api_key=api_key,source_system=cloud_watch_source)
        file_log_impl = FileLogImplementation()
        # console_log_impl = ConsoleLogImplementation()
        self.app_logger=ApplicationLogger(cloud_log_impl, int(logging_level))
        self.user_change_logger=UserChangeLogLogger(file_log_impl,int(logging_level))
        self.app_logger.info("Application base Initialized")
        