import smtplib, ssl
from email.mime.multipart import MIMEMultipart, MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os
import email
from ..interfaces import MessengerBase

class Gmail:
    def __init__(self, sender_address, receiver_address):
        self._sender_address = sender_address
        self._receiver_address = receiver_address

    @property
    def sender_address(self):
        print("Gmail sender address has been set")
        return self._sender_address

    @property
    def receiver_address(self):
        print("Gmail receiver address has been set")
        return self._receiver_address

    @sender_address.setter
    def sender_address(self, address):
        # TODO: Email regex
        print(f"Setting Gmail sender address to: {address}")
        self._sender_address = address

    @receiver_address.setter
    def receiver_address(self, address):
        # TODO: Email regex
        print(f"Setting Gmail receiver address to: {address}")
        self._receiver_address = address

    def send_logs(self, file):
        subject = 'some subject message'
        body = """text body of the email"""