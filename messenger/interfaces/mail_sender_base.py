class MailSenderBase:
    def __init__(self):
        self._email = ""

    @property
    def email(self):
        print("Email has been set")
        return self._email

    @email.setter
    def email(self, address):
        # TODO: Email regex
        print(f"Setting gmail address to: {address}")
        self._email = address

