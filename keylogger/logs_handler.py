"""
Tutorial context managers: https://www.geeksforgeeks.org/context-manager-in-python/
"""

from .interfaces import LogsBase


class LogsHandler(LogsBase):
    def __init__(self):
        self.logs_file = ""
        self._open_mode = "a+"

    def __enter__(self):
        self.file = open(self.logs_file, self._open_mode)
        return self.file

    def __exit__(self):
        self.file.close()

    def add_header(self):
        pass

    def _add_datetime(self):
        pass

    def _create_header(self):
        pass
