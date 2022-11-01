import cv2
from pyautogui import screenshot
from numpy import array
from win32api import GetSystemMetrics
from threading import Thread


class ScreenRecorder:
    def __init__(self, length=20, out_video="screen_record.avi"):
        self.length = length
        self._fps = 20
        self.out_video = out_video
        self.video_width = GetSystemMetrics(0)
        self.video_height = GetSystemMetrics(1)
        self.video_codec = cv2.VideoWriter_fourcc(*'XVID')

    def start(self):
        Thread(target=self._start).start()

    def _start(self):
        video_writer = cv2.VideoWriter(self.out_video, self.video_codec, 20.0, (self.video_width, self.video_height))

        for _ in range(self.length * self._fps):
            screenshoot_array = array(screenshot())
            frame = cv2.cvtColor(screenshoot_array, cv2.COLOR_BGR2RGB)
            video_writer.write(frame)

        video_writer.release()
        cv2.destroyAllWindows()