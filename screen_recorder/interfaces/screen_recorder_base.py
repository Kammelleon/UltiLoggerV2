from abc import ABC, abstractmethod


class ScreenRecorderBase(ABC):

    @abstractmethod
    def start(self):
        pass
