"""
Tutorial context managers: https://www.geeksforgeeks.org/context-manager-in-python/
"""
import datetime
import platform
from requests import get
from .interfaces import LogsBase
import getpass
import socket
import re
import uuid
import os

class LogsHandler(LogsBase):
    def __init__(self):
        self.logs_file = ""
        self.open_mode = "a+"

    def __enter__(self):
        self.file = open(self.logs_file, self.open_mode)
        return self.file

    def __exit__(self):
        self.file.close()

    def add_header(self):
        with open(self.logs_file, self.open_mode) as log_file:
            log_file.write(self._create_header())

    def _add_datetime(self):
        pass

    def _create_header(self):
        current_date = self._get_current_date()
        header = f"-------------System-Information-------------\n" \
                 f"Date: {current_date}\n" \
                 f"User: {getpass.getuser()}\n" \
                 f"System: {platform.system()} {platform.version()}\n" \
                 f"Computer name: {platform.node()}\n" \
                 f"Local IP: {socket.gethostbyname(socket.gethostname())}\n" \
                 f"MAC address: {':'.join(re.findall('..', '%012x' % uuid.getnode()))}\n" \
                 f"Public IP {get('https://api.ipify.org').text}\n" \
                 f"--------------------------------------------\n"
        return header

    def _get_current_date(self):
        return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")