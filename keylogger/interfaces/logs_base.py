from abc import ABC, abstractmethod


class LogsBase(ABC):

    @abstractmethod
    def __enter__(self):
        """"""

    @abstractmethod
    def __exit__(self):
        """"""

    @abstractmethod
    def add_header(self):
        """"""

    @abstractmethod
    def _add_datetime(self):
        """"""
