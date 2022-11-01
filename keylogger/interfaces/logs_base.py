from abc import ABC, abstractmethod


class LogsBase(ABC):
    @abstractmethod
    def add_header(self):
        """Adds a header on every new keylogger session"""

    @abstractmethod
    def add_datetime(self):
        """Adds datetime periodically to log file"""
