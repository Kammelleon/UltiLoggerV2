from abc import ABC, abstractmethod


class KeyloggerBase(ABC):

    @abstractmethod
    def on_key_press(self):
        """"""

    @abstractmethod
    def start_key_press_listener(self):
        """"""