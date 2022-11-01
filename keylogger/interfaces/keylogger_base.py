from abc import ABC, abstractmethod


class KeyloggerBase(ABC):

    @abstractmethod
    def _on_key_press(self, pressed_key):
        """Handles actions that should happen after user pressed some key"""

    @abstractmethod
    def start_listener(self):
        """Starts keylogger (pynput listener)"""
