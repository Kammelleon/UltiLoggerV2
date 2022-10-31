"""
Tutorial context managers: https://www.geeksforgeeks.org/context-manager-in-python/
"""

from interfaces import LogsBase


class LogsHandler(LogsBase):
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self):
        self.file.close()