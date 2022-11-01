from abc import ABC, abstractmethod


class LogsBase(ABC):
    @abstractmethod
    def add_header(self):
        """"""

    @abstractmethod
    def add_datetime(self):
        """"""
