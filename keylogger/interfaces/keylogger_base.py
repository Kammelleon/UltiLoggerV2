from abc import ABC, abstractmethod


class KeyloggerBase(ABC):

    @abstractmethod
    def _on_key_press(self, pressed_key):
        """"""

    @abstractmethod
    def start_listener(self):
        """"""
